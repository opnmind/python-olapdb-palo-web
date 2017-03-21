# -*- coding: utf-8 -*-
from __future__ import print_function

class Cube(object):
    def __init__(self, Connection, APIOutput):
        APIOutput = APIOutput.split(';')
        self.Sid = Connection.Sid
        self.Client = Connection.Client
        self.getUrlResult = Connection.getUrlResult
        self.getDatabaseUrlRequest = Connection.getDatabaseUrlRequest
        self.ServerRoot = Connection.ServerRoot
        self.getCube = Connection.getCube
        self.__DataBaseID = Connection.getID()
        self.__ID = APIOutput[0]
        self.__Name = APIOutput[1][1:-1]
        self.__NumDimensions = APIOutput[2]
        self.__DimensionsIDList = APIOutput[3].split(',')
        self.__DimensionsList = {}
        self.__DimensionsListByName = {}
        self.__NumCells = APIOutput[4]
        self.__NumFilledCells = APIOutput[5]
        self.__Status = APIOutput[6]
        self.__Type = APIOutput[7]
        self.__Token = APIOutput[8]
        self.__Rules = {}
        self.isSystemCube = True if ('#_' in self.__Name) else False
        self.getDimensionByID = Connection._getFullLoadedDimension
        self.LoadRules()
        self.LoadCubeDimensions()

    def getDataBaseID(self):
        return self.__DataBaseID

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__Name

    def getNumDimensions(self):
        return self.__NumDimensions

    def getDimensionsList(self):
        return self.__DimensionsList

    def getDimensionsIDList(self):
        return self.__DimensionsIDList

    def getDimensionsNameList(self):
        return [self.__DimensionsList[DimID].getName() for DimID in self.__DimensionsIDList]

    def getDimensionByName(self, Name):
        ID = self.__DimensionsListByName[Name]
        return self.__DimensionsList[ID]

    def DimensionExists(self, Name):
        return Name in self.__DimensionsListByName

    def getNumCells(self):
        return self.__NumCells

    def getNumFilledCells(self):
        return self.__NumFilledCells

    def getStatus(self):
        return self.__Status

    def getType(self):
        return self.__Type

    def getToken(self):
        return self.__Token

    def getAttrDimension(self):
        if self.isSystemCube:
            AttrDimName = self.getName() + '_'
            return self.getDimensionByName(AttrDimName)
        else:
            return False

    def getCubeUrlRequest(self, CMD, Param = {}):
        Param['cube'] = self.getID()
        return self.getDatabaseUrlRequest(CMD, Param)

    def LoadRules(self):
        CMD = 'cube/rules'
        Url = self.getCubeUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        for Row in r.data.decode('utf-8').split('\n')[:-1]:
            ID, Definition, ExtID = Row.split(';')[:3]
            self.__Rules[str(ID)] = Definition[1:-1]

    def LoadCubeDimensions(self):
        for ID in self.__DimensionsIDList:
            self.__DimensionsList[ID] = self.getDimensionByID(ID)
            self.__DimensionsListByName[self.getDimensionByID(ID).getName()] = ID

    def getRules(self):
        return self.__Rules

    def getRuleID(self, Definition):
        for ID, R in self.getRules().items():
            if R == Definition:
                return ID

    def CreateRule(self, Definition):
        CMD = 'rule/create'
        Param = {'definition': Definition.replace('""', '"')}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def ParseRule(self, Definition):
        CMD = 'rule/parse'
        Param = {'definition': Definition.replace('""', '"')}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def Load(self):
        CMD = 'cube/load'
        Url = self.getCubeUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def Unload(self):
        CMD = 'cube/unload'
        Url = self.getCubeUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def Destroy(self):
        CMD = 'cube/destroy'
        Url = self.getCubeUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def Save(self):
        CMD = 'cube/save'
        Url = self.getCubeUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def getCellPath(self, Coordinates):
        CellPath = []
        if not type(Coordinates) == tuple:
            Coordinates = (Coordinates, )
        for i, Coord in enumerate(Coordinates):
            ID = self.getDimensionsIDList()[i]
            Dim = self.getDimensionByID(ID)
            CellPath.append(str(Dim.getElementID(Coord)))
        return ','.join(CellPath)

    def getAreaPath(self, Coordinates):
        ElementsID = []
        AreaPath = []
        for i, Elements in enumerate(Coordinates):
            ID = self.getDimensionsIDList()[i]
            Dim = self.getDimensionByID(ID)
            ElementsID = []
            if not type(Elements) == tuple:
                if Elements == '*':
                    AreaPath.append(Elements)
                else:
                    ElementsID = Dim.getElementID(Elements)
                    if not ElementsID == False:
                        AreaPath.append(str(ElementsID))
                    else:
                        return False
#                    AreaPath.append(str(Dim.getElementID(Elements)))
            else:
                for E in Elements:
                    IDElem = Dim.getElementID(E)
                    if not IDElem == False:
                        ElementsID.append(str(IDElem))
                AreaPath.append(':'.join(ElementsID))
        return ','.join(AreaPath)

    def getValuePath(self, Values):
        return ':'.join([str(Value) for Value in Values])

    def Replace(self, Coordinate, Value, Splash = 0):
        CMD = 'cell/replace'
        Path = self.getCellPath(Coordinate)
        Param = {'path': Path,
                 'value': str(Value),
                 'splash': Splash}
        Url = self.getCubeUrlRequest(CMD, Param)
        try:
            r = self.Client.request('GET', Url)
        except:
            return False
        self.Save()
        return r.data.decode('utf-8')

    def ReplaceBulk(self, Coordinates, Values, Splash = 0):
        CMD = 'cell/replace_bulk'
        Paths = self.getAreaPath(Coordinates)
        Values = self.getValuePath(Values)
        Param = {'paths': Paths,
                 'values': Values,
                 'splash': Splash}
        Url = self.getCubeUrlRequest(CMD, Param)
        try:
            r = self.Client.request('GET', Url)
        except:
            return False
        return r.data.decode('utf-8')

    def Clear(self, Coordinates):
        CMD = 'cube/clear'
        Path = self.getAreaPath(Coordinates)
        if Path == False:
            return False
        Param = {'area': Path}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8')

    def getValue(self, Coordinates):
        CMD = 'cell/value'
        Path = self.getCellPath(Coordinates)
        Param = {'path': Path}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8').split(';')[2]

    def getValueByID(self, CoordinatesID):
        CMD = 'cell/value'
        Path = ','.join([str(ID) for ID in CoordinatesID])
        Param = {'path': Path}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8').split(';')[2].replace('"', '')

    def getArea(self, Coordinates):
        CMD = 'cell/area'
        Path = self.getAreaPath(Coordinates)
        Param = {'area': Path}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8').split('\n')[:-1]

    def getValues(self, Coordinates, ForceEmptyCells = False):
        CMD = 'cell/values'
        Paths = ''
        for CellPath in self.getArea(Coordinates):
            CellTuple = CellPath.split(';')
            if CellTuple[2] != '' or ForceEmptyCells == True:
                Paths = Paths + CellTuple[-2] + ':'
        Paths = Paths[:-1]
        Param = {'paths': Paths}
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)

        Values = []
        for Rec in Res.data.decode('utf-8').split('\n')[:-1]:
            Value = Rec.split(';')[-2].replace('"', '')
            Values.append(Rec.split(';')[-2].replace('"', ''))
        return Values
#        return [Rec.split(';')[-2].replace('"', '') for Rec in Res.data.split('\n')[:-1]]

    def Export(self, Coord = None, Condition = None, BlockSize = 1000000):
        CMD = 'cell/export'
        Param = {'blocksize': BlockSize,
                 'use_rules': 1}
        if Coord:
            Param ['area'] = self.getAreaPath(Coord)
        if Condition:
            Param ['condition'] = Condition
        Url = self.getCubeUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8').split('\n')[:-2]

    def Dump(self, Coord = None, Condition = None):
        Res = []
        Export = self.Export(Coord, Condition)
        for Cell in Export:
            NewRec = []
            CellRec = Cell.split(';')[:-1]
            CellValue = CellRec[2]
            CellCoord = CellRec[3].split(',')
            for DimID, ElementID in zip(self.getDimensionsIDList(), CellCoord):
                NewRec.append(self.getDimensionByID(DimID).getElementName(ElementID))
            NewRec.append(CellValue)
            Res.append(NewRec)
        return Res

    def DumpCell(self, Coord = None, Condition = None, UseKeyDWIfExists = True):
        return CubeDumpIterator(self, self.Export(Coord, Condition), UseKeyDWIfExists)

    def DumpCellAsObject(self, Coord = None, Condition = None, UseKeyDWIfExists = True):
        return CubeDumpIteratorObject(self, self.Export(Coord, Condition), UseKeyDWIfExists)


## ##
class CubeDumpCell():
    def __init__(self, MethodList):
        self.MethodList = MethodList
        self.MethodList.append('Value')
    def __repr__(self):
        ReprStr = ''
        for Method in self.MethodList:
            ReprStr = ReprStr + getattr(self, Method) + ', '
        return ReprStr[:-3]

## Iteratore per la funzione Dump##
class CubeDumpIterator():

    def __init__(self, CubeObj, Export, UseKeyDWIfExists):
        self.Export = Export
        self.index = 0
        self.loop = len(Export) -1
        self.CubeObj = CubeObj
        self.UseKeyDWIfExists = UseKeyDWIfExists
        if UseKeyDWIfExists:
            self._setDumpSchema()

    def __iter__(self):
        return self

    def next(self):
        if len(self.Export) == 0:
            raise(StopIteration)
        if self.index == self.loop:
            raise(StopIteration)

        if self.UseKeyDWIfExists:
            Record = self._getRecord()
            while not Record:
                Record = self.next()
            return Record
        else:
            return self._getSimpleRecord()

    def _setDumpSchema(self):
        if len(self.Export) == 0:
            return False
        Record = self.Export[0].split(';')[:-1][3].split(',')
        AttributeValues = {}
        for DimID, ElementID in zip(self.CubeObj.getDimensionsIDList(), Record):
            Dim = self.CubeObj.getDimensionByID(DimID)
            AttrCubeName = Dim.getAttributeCubeName()
            AttrCube = self.CubeObj.getCube(AttrCubeName)
            AttributeValues[DimID] = dict(zip(Dim.getElementsIDList(), Dim.getElementsNameList()))

            ## Overriding del dictionary AttributeValues per i cubi di attributi e di sistema
            if AttrCube and AttrCube.isSystemCube:
                AttrDim = AttrCube.getAttrDimension()
                if AttrDim.KeyDataWarehouseExists():
                    AttributeValues[DimID] = {}
                    CubeExport = AttrCube.Export(((AttrDim.getKeyDWName()), ('*')), None)
                    for Cell in CubeExport:
                        CellRec = Cell.split(';')[:-1]
                        Value = str(CellRec[2]).replace('"', '')
                        Skip, ElementID = CellRec[3].split(',')
                        AttributeValues[DimID][ElementID] = Value
        self.AttributeValues = AttributeValues
        self.DimensionsIDList = self.CubeObj.getDimensionsIDList()

    def _getSimpleRecord(self):
        Rec = []
        Coord, Value = self._getCoordAndValue()
        for DimID, ElementID in zip(self.CubeObj.getDimensionsIDList(), Coord):
            Dim = self.CubeObj.getDimensionByID(DimID)
            Rec.append(Dim.getElementName(ElementID))
        Rec.append(Value)
        return Rec

    def _getRecord(self):
        Rec = []
        Coord, Value = self._getCoordAndValue()
        for DimID, ElementID in zip(self.DimensionsIDList, Coord):
            if ElementID in self.AttributeValues[DimID]:
                Rec.append(self.AttributeValues[DimID][ElementID])
            else:
                return False
        Rec.append(Value)
        return Rec

    def _getCoordAndValue(self):
        Cell = self.Export[self.index]
        self.index = self.index + 1
        CellRec = Cell.split(';')[:-1]
        Value = CellRec[2]
        Coord = CellRec[3].split(',')
        return Coord, Value


class CubeDumpIteratorObject(CubeDumpIterator):
    def __init__(self, CubeObj, Export, UseKeyDWIfExists):
        CubeDumpIterator.__init__(self, CubeObj, Export, UseKeyDWIfExists)
        self.CubeCell = CubeDumpCell(CubeObj.getDimensionsNameList())

    def _getSimpleRecord(self):
        Coord, Value = self._getCoordAndValue()
        for DimID, ElementID in zip(self.CubeObj.getDimensionsIDList(), Coord):
            Dim = self.CubeObj.getDimensionByID(DimID)
            ElementValue = Dim.getElementName(ElementID)
            setattr(self.CubeCell, Dim.getName(), ElementValue)
        setattr(self.CubeCell, 'Value', Value)
        return self.CubeCell

## Nuova versione
    def _getRecord(self):
        Coord, Value = self._getCoordAndValue()
        for DimID, ElementID in zip(self.DimensionsIDList, Coord):
            Dim = self.CubeObj.getDimensionByID(DimID)
            if ElementID in self.AttributeValues[DimID]:
                ElementValue = self.AttributeValues[DimID][ElementID]
                setattr(self.CubeCell, Dim.getName(), ElementValue)
            else:
                print("Le seguenti cooridnate sono inesistenti: ", DimID, ElementID)
                return False
        setattr(self.CubeCell, 'Value', Value)
        return self.CubeCell

## Originale
##    def _getRecord(self):
##        Coord, Value = self._getCoordAndValue()
##        for DimID, ElementID in zip(self.DimensionsIDList, Coord):
##            Dim = self.CubeObj.getDimensionByID(DimID)
##            try:
##                ElementValue = self.AttributeValues[DimID][ElementID]
##            except:
##                print DimID, ElementID
##            setattr(self.CubeCell, Dim.getName(), ElementValue)
##        setattr(self.CubeCell, 'Value', Value)
##        return self.CubeCell
