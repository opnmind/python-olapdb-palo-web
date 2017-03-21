from PyJedoxWebApi.Cube import Cube
from PyJedoxWebApi.Dimension import Dimension

class DataBase():
    def __init__(self, Interface, APIOutput):
        self.Sid = Interface.Sid
        self.Client = Interface.Client
        self.getUrlResult = Interface.getUrlResult
        self.UrlEncoder = Interface.UrlEncoder
        self.ServerRoot = Interface.ServerRoot
        APIOutput = APIOutput.split(';')
        self.__ID = APIOutput[0]
        self.__Name = APIOutput[1][1:-1]
        self.__NumDimensions = APIOutput[2]
        self.__NumCubes = APIOutput[3]
        self.__isSystem = bool(APIOutput[5])
        self.__Token = APIOutput[6]
        self.__DimensionsList = {}
        self.__CubesList = {}
        self.__DimensionsDictionary = {}
        self.__CubesDictionary = {}
        self.loadDimensions()
        self.loadCubes()

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__Name

    def getNumDimensions(self):
        return self.__NumDims

    def getNumCubes(self):
        return self.__NumCubes

    def getToken(self):
        return self.__Token

    def isSystem(self):
        return self.__isSystem

    def isSystemObject(self, PaloOutput):
        if "#_#_" in PaloOutput.split(";")[1]:
            return True

    def loadDimensions(self):
        CMD = 'database/dimensions'
        Param = {'show_attribute': 1,
                 'show_system': 0}
        Url = self.getDatabaseUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        for Row in r.data.decode('utf-8').split('\n')[:-1]:
            if not self.isSystemObject(Row):
                DimObj = Dimension(self, Row)
                self.__DimensionsList[DimObj.getName()] = DimObj
                self.__DimensionsDictionary[str(DimObj.getID())] = DimObj.getName()

    def loadCubes(self):
        CMD = 'database/cubes'
        Param = {'show_attribute': 1,
                 'show_system': 0}
        Url = self.getDatabaseUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        for Row in r.data.decode('utf-8').split('\n')[:-1]:
#            if int(Row.split(';')[4]) > 0:
#                CubeObj = Cube(self, Row)
#                self.__CubesList[CubeObj.getName()] = CubeObj
#                self.__CubesDictionary[str(CubeObj.getID())] = CubeObj.getName()
            if not self.isSystemObject(Row):
                CubeObj = Cube(self, Row)
                self.__CubesList[CubeObj.getName()] = CubeObj
                self.__CubesDictionary[str(CubeObj.getID())] = CubeObj.getName()

    def getDimension(self, DimensionName):
        if DimensionName in self.__DimensionsList:
            return self.__DimensionsList[DimensionName]
        else:
            return False

    def getDimensionsID(self, DimensionsList):
        return [self.getDimension(DimName).getID() for DimName in DimensionsList]

    def getDimensionNameByID(self, ID):
        ID = str(ID)
        return self.__DimensionsDictionary[ID]

    def _getFullLoadedDimension(self, ID):
        ID = str(ID)
        Name = self.getDimensionNameByID(ID)
        Dim = self.__DimensionsList[Name]
        if Dim.isLoaded():
            return Dim
        else:
            Dim.loadElements()
            return self.__DimensionsList[Name]

    def dropDimension(self, Name):
        CMD = 'dimension/destroy'
        Param = {'dimension': self.getDimension(Name).getID()}
        Url = self.getDatabaseUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        del self.__DimensionsDictionary[Name]

    def clearDimension(self, Name):
        r = self.getDimension(Name).Clear()

    def getCube(self, CubeName):
        if CubeName in self.__CubesList:
            return self.__CubesList[CubeName]
        else:
            return False

    def Save(self, Param = {}):
        CMD = 'database/save'
        Url = self.getDatabaseUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        return r

    def CreateDimension(self, DimensionName, DimensionType = 0):
        CMD = 'dimension/create'
        Param = {'type': DimensionType,
                 'new_name': DimensionName}
        Url = self.getDatabaseUrlRequest(CMD, Param)
        if not self.getDimension(DimensionName):
            r = self.Client.request('GET', Url)
            Row = r.data.decode('utf-8')
            DimObj = Dimension(self, Row)
            self.__DimensionsList[DimObj.getName()] = DimObj
            self.__DimensionsDictionary[str(DimObj.getID())] = DimObj.getName()
            return DimObj
        else:
            print('dimension name in use')
            return self.getDimension(DimensionName)

    def CreateCube(self, CubeName, DimensionsList, CubeType = 0):
        CMD = 'cube/create'
        Param = {'type': CubeType,
                 'new_name': CubeName,
                 'dimensions': ','.join(self.getDimensionsID(DimensionsList))}
        Url = self.getDatabaseUrlRequest(CMD, Param)
        if not self.getCube(CubeName):
#        try:
            r = self.Client.request('GET', Url)
            Row = r.data.decode('utf-8')
            CubeObj = Cube(self, Row)
            self.__CubesList[CubeObj.getName()] = CubeObj
            self.__CubesDictionary[str(CubeObj.getID())] = CubeObj.getName()
            return CubeObj
#        except:
        else:
            print('cube name in use')
            return self.getCube(CubeName)

    def getDatabaseUrlRequest(self, CMD, Param = {}):
        UrlRequest = self.ServerRoot + CMD + '?sid=' + self.Sid + '&database=' + self.getID()
        #print UrlRequest + '&' + self.UrlEncoder(Param)
        return UrlRequest + '&' + self.UrlEncoder(Param)

    def _noErrors(self, PaloOutput):
        ErrorDictionary = {'3005': 'dimension name in use',
                           '5008': 'cube name in use'}
        ErrorCode = PaloOutput[0].split(';')[0]
        if ErrorCode in ErrorDictionary:
            return ErrorDictionary[ErrorCode]
        else:
            return True
