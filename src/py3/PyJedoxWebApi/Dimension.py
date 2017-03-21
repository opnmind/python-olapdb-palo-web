# -*- coding: utf-8 -*-
from __future__ import print_function

class Dimension(object):
    def __init__(self, Connection, APIOutput):
        APIOutput = APIOutput.split(';')
        self.Sid = Connection.Sid
        self.Client = Connection.Client
        self.getUrlResult = Connection.getUrlResult
        self.getDatabaseUrlRequest = Connection.getDatabaseUrlRequest
        self.ServerRoot = Connection.ServerRoot
        self.__DataBaseID = Connection.getID()
        self.__ID = APIOutput[0]
        self.__Name = APIOutput[1][1:-1]
        self.__NumElements = APIOutput[2]
        self.__Type = self._getType(APIOutput[6])
        self.__AttributeCubeID = APIOutput[8]
        self.__AttributeCubeName = self._getAttrCubeName()
        self.__Token = APIOutput[10]
        self.__Elements = {}
        self.__ElementsByID = {}
        self.__ElementsIDList = []
        self.__isLoaded = False

    def getDataBaseID(self):
        return self.__DataBaseID

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__Name

    def getNumElements(self):
        return self.__NumElements

    def getType(self):
        return self.__Type

    def getAttributeCubeID(self):
        return self.__AttributeCubeID

    def getAttributeCubeName(self):
        return self.__AttributeCubeName

    def getToken(self):
        return self.__Token

    def getDimensionUrlRequest(self, CMD, Param = {}):
        Param['dimension'] = self.getID()
        return self.getDatabaseUrlRequest(CMD, Param)

    def _getAttrCubeName(self):
        CMD = 'cube/info'
        ID = self.getAttributeCubeID()
        if len(ID) > 0:
            Param = {'cube': self.getAttributeCubeID()}
            Url = self.getDatabaseUrlRequest(CMD, Param)
            r = self.Client.request('GET', Url)
            return r.data.decode('utf-8').split(';')[1].replace('"', '')
        else:
            return False

    def isLoaded(self):
        return self.__isLoaded

    def loadElements(self):
        CMD = 'dimension/elements'
        Url = self.getDimensionUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        List = r.data.decode('utf-8').split('\n')[:-1]
        for Element in List:
            ID, Name = Element.split(';')[:2]
            self.__Elements[Name[1:-1]] = str(ID)
            self.__ElementsByID[str(ID)] = Name[1:-1]
            self.__ElementsIDList.append(str(ID))
            #self.__ElementsAliasByID[str(ID)]['alias_name'] = 'alias_value'
        self.__isLoaded = True

    def addElement(self, ElementName, ElementType = 1):
        CMD = 'element/create'
        Param = {'new_name': ElementName,
                 'type': ElementType,}
        if ElementType == 4:
            Dict = {}
            for C, P in zip(ChildrenElement, ParentElement):
                if self.getElementID(C):
                    Dict.setdefault(P, set()).add(self.getElementID(C))
            for Element, Children in Dict.iteritems():
                Param['children'] =  ','.join(Children)
                Url = self.getDimensionUrlRequest(CMD, Param)
                r = self.Client.request('GET', Url)
                print(r.data.decode('utf-8').split('\n')[:-1])
        else:
            if not self.getElementID(ElementName):
                Url = self.getDimensionUrlRequest(CMD, Param)
                r = self.Client.request('GET', Url)
                Row = r.data.decode('utf-8')
                ID = Row.split(';')[0]
                self.__Elements[ElementName] = str(ID)
                self.__ElementsByID[str(ID)] = ElementName
                self.__ElementsIDList.append(ID)
                return ID
            else:
                print("element name '" + ElementName + "' in use with ID '" + self.getElementID(ElementName) + "'")
                return self.getElementID(ElementName)

    def Consolidate(self, ChildrenElement, ParentElement):
        CMD = 'element/create'
        Dict = {}
        for C, P in zip(ChildrenElement, ParentElement):
            if self.getElementID(C):
                Dict.setdefault(P, set()).add(self.getElementID(C))

        for Element, Children in Dict.iteritems():
            Param = {'new_name': Element,
                     'type': 4,
                     'children': ','.join(Children)}
            Url = self.getDimensionUrlRequest(CMD, Param)
            r = self.Client.request('GET', Url)
            print(r.data.decode('utf-8').split('\n')[:-1])

    def getElements(self):
#        return self.__Elements
        for ID in self.__ElementsIDList:
            yield ID, self.__ElementsByID[ID]

    def getElementsName(self):
#        return self.__Elements.keys()
        for ID in self.__ElementsIDList:
            yield self.__ElementsByID[ID]

    def getElementID(self, Name):
        if Name in self.__Elements:
            return self.__Elements[Name]
        else:
            return False

    def getElementsIDList(self):
        return self.__ElementsIDList

    def getElementsNameList(self):
        return [self.__ElementsByID[ID] for ID in self.__ElementsIDList]

    def getKeyDW(self):
        return self.__Elements['KeyDW']

    def getKeyDWName(self):
        return 'KeyDW'

    def getElementName(self, ID):
        return self.__ElementsByID[ID]

    def ElementExists(self, Name):
        return Name in self.__Elements

    def KeyDataWarehouseExists(self):
        return 'KeyDW' in self.__Elements

    def deleteElement(self, Name):
        CMD = 'element/destroy'
        Param = {'element': self.getElementID(Name)}
        Url = self.getDimensionUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)

    def MoveElement(self, Name, NewPosition):
        CMD = 'element/move'
        Param = {'element': self.getElementID(Name),
                 'position': NewPosition}
        Url = self.getDimensionUrlRequest(CMD, Param)
        r = self.Client.request('GET', Url)
        return r.data.decode('utf-8').split('\n')[:-1]

    def Clear(self):
        CMD = 'dimension/clear'
        Url = self.getDimensionUrlRequest(CMD)
        r = self.Client.request('GET', Url)
        return r

    def _getType(self, TypeID):
        TypeDict = {"0": "NORMAL", "1": "SYSTEM", "2": "ATTRIBUTE", "3":"USER_INFO"}
        return TypeDict[TypeID]
