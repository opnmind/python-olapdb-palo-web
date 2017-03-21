# -*- coding: utf-8 -*-
from __future__ import print_function
from PyJedoxWebApi.PyJedoxWeb import PyJedoxWeb

P = PyJedoxWeb()
print("SID: " + P.getSid())

database = "control_musterstadt"
cubename = "fcmain"
res = P.CreateDatabase(DBName=database)
print(res)

P.loadDBList()
DB = P.getDB(DBName=database)
DB.loadDimensions()
DB.loadCubes()

DimTest1_Jahre = DB.CreateDimension('Jahre')
DimTest2_Datenart = DB.CreateDimension('Datenart')
DimTest3_Firma = DB.CreateDimension('Firma')
DimTest4_Einheit = DB.CreateDimension('Einheit')
DimTest5_Periode = DB.CreateDimension('Periode')
DimTest6_Position = DB.CreateDimension('Position')
Cubetest = DB.CreateCube(cubename, ('Jahre','Datenart','Firma','Einheit','Periode','Position'))

print(DimTest1_Jahre.addElement("2005"))
print(DimTest1_Jahre.addElement("2006"))
print(DimTest1_Jahre.addElement("2008"))
print(DimTest1_Jahre.addElement("2007"))
print(DimTest1_Jahre.addElement("2009"))
print(DimTest1_Jahre.addElement("2010"))
print(DimTest1_Jahre.addElement("2011"))
print(DimTest1_Jahre.addElement("2012"))

print(DimTest2_Datenart.addElement("Ist"))
print(DimTest2_Datenart.addElement("Plan"))

print(DimTest3_Firma.addElement("SWH"))
print(DimTest3_Firma.addElement("KWL"))

print(DimTest4_Einheit.addElement("Euro"))
print(DimTest4_Einheit.addElement("Anzahl"))

print(DimTest5_Periode.addElement("Jahr"))
print(DimTest5_Periode.addElement("Januar"))
print(DimTest5_Periode.addElement("Februar"))
print(DimTest5_Periode.addElement("März"))
print(DimTest5_Periode.addElement("April"))
print(DimTest5_Periode.addElement("Mai"))
print(DimTest5_Periode.addElement("Juni"))
print(DimTest5_Periode.addElement("Juli"))
print(DimTest5_Periode.addElement("August"))
print(DimTest5_Periode.addElement("September"))
print(DimTest5_Periode.addElement("Oktober"))
print(DimTest5_Periode.addElement("November"))
print(DimTest5_Periode.addElement("Dezember"))

print(DimTest6_Position.addElement("Bilanz"))
print(DimTest6_Position.addElement("GuV"))

Cubetest.Save()


P.loadDBList()
DB = P.getDB(DBName=database)
DB.loadDimensions()
DB.loadCubes()

C = DB.getCube(cubename)
if C == False:
    print(cubename + " konnte nicht geladen werden...")
    quit()
else:
    print(C.getID())

## Delete all elements of the dimension ##
#C.clearDimension('')

D = DB.getDimension("Firma")
print(D.getAttributeCubeName())

for ID in C.getDimensionsIDList():
    DimName = DB.getDimensionNameByID(ID)
    Dim = DB.getDimension(DimName)
    Dim.loadElements()

    ## Loop through dictionary (not ordered) of the elements of the dimension ##
    ## the key if the name of the element, the value is the internal ID of the element ##
    for key, val in Dim.getElements().__iter__():
        print(key, val)

    ## Loop through (not ordered) elements name of the dimension ##
    for E in Dim.getElements():
        print(E)

    ## Loop through (ordered) elements internal ID of the dimension ##
    for ID in Dim.getElementsIDList():
        print(ID)

Dim = C.getDimensionByID(17)
print(C.getDimensionByID(17).getElements())


Dim = DB.getDimension('Jahre')
Dim.loadElements()
Lst = Dim.getElementsName()

Lst = sorted(Lst)
## Sort the elements of the dimension ##
for Pos, Name in enumerate(Lst):
    print(Pos, Name)
    print(Dim.MoveElement(Name, Pos))


## Write rule into the cube ##
R = """['Jahr'] = ['Januar'] + ['Februar'] + ['März']"""
print(C.ParseRule(R))
C.CreateRule(R)

## loop through the rules of the cube and execute the 'rule/parse' web api##
Rules = C.getRules()
for R in Rules.values():
    print(C.ParseRule(R))

#####################################################################################################

quit()
Coord = (('*'), ('some element', 'other element', 'etc'), ('*'), ('*'), ('*'))
Condition = '>= 0.1 xor <=-0.1'

## Return the output of the cell/export web api ##
Res = C.Dump(Coord)
print(Res)

## Delete all cell of cube subset ##
C.Clear(Coord)

## Save the cube ##
C.Save()


## Return a list of tuples with the cells value  ##
print(C.getValues(Coord))

## Loop through the cube subset and return a tuple with coordinates and the value for each cell ##
for Cell in C.DumpCell(Coord):
    print(Cell)

## Loop through the cube subset and return an object for each cell ##
## To access the cell value use the "Value" property; to access to the element name ##
## use the "DimensionName" ##
## By default, DumpCellAsObject and DumpCell methods have the "UseKeyDWIfExists" parameter setted to true.
## When the parameter "UseKeyDWIfExists" is setted to true the method "DumpCellAsObject" will look for an "attribute"
## called "KeyDW" for each dimension  (the name of the "attribute" is setted in PyPaloWebConfig module
## with the property "__DatawarehouseAliasName") and if such "attribute" will be found, the method will return
## the value of the "attribute" instead of the element name.
## This function is useful to make the output of dump directly loadable in my datawharehouse, in which the elements are identified by canonical "ID number"
for CellObj in C.DumpCellAsObject(Coord):
    print(CellObj.Dim1, CellObj.Dim2, CellObj.DimN, CellObj.Value)
