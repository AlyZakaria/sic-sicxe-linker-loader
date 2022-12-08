from Linker_Loader import loadMap
from operator import *
from Absolute_Loader import helper_function as hf
from Linker import linker
import re



def getrow(orgAddress):
    startMem = linker.starting_mem_address
    rowAdress = orgAddress[:3] + '0'
    index = hf.get_row(rowAdress,startMem)
    return index

def getObjectCode(strow, stcol, size, df):
    objCode = ''
    flag = True
    flag_2 = False
    for row in range(strow, strow + 2, 1):
        for column in range(stcol, 17):
            if len(objCode) == 6 and not size:
                flag_2 = True
                break
            elif len(objCode) == 5 and size:
                flag_2 = True
                break
            if flag and size:
                objCode += df.iloc[row,column][1]
                flag = False
            else:
                objCode += df.iloc[row,column]
        stcol = 1
        if flag_2:
            break
    return objCode


def getCell(stAddress, stRec, df):
    orgAddress = hex(add(int(stAddress,16), int(str(stRec),16)))[2:].upper()
    # get row & col
    row = getrow(orgAddress)
    col = df.columns.get_loc(orgAddress[3])
    return[row , col]


def insertObjCode(strow, stcol, objCode, df):
    flag = True
    flag_2 = False
    i = 0
    for row in range(strow, strow + 2, 1):
        for col in range(stcol, 17):
            if i == len(objCode):
                flag_2 = True
                break
            if flag and len(objCode) == 5:
                df.iloc[row, col] = (df.iloc[row,col][0] + objCode[i]).upper() 
                flag = False
                i += 1
            else:
                df.iloc[row,col] = objCode[i:i+2].upper()
                i += 2          
        stcol = 1
        if flag_2:
            break
           
def modify(map, df):
    for key in map:
        [row, col] = getCell('0000' , key, df)
        insertObjCode(row, col , map[key] , df)



def modifyMemory(df, df_Loader):
    obj_map = {}
    startAddress = df.iloc[0,0]
    map = loadMap.symbolMap(df_Loader)
    flag = False
    f = open('rsc\\sicxe.txt', 'r')
    # print(loadMap.modifiedRec)
    secHead = False
    for i in f.readlines():

        if i[0] == 'H' and secHead:
            startAddress = map[i[1:7]]
        if i[0] == 'M':
            startRec = i[1:7]
            SymbolName = i[10:-1].ljust(6)
            sign = i[9]
            if i[8] == '5':
                flag = True
            # to get the cell 
            [row , col] = getCell(startAddress, startRec, df)
            #get target object code
            objCode = getObjectCode(row, col, flag, df)
            key = hex(add(int(startRec,16) , int(startAddress,16)))[2:] 
            # modified ObjectCode
            if sign == '+':
                # print(objCode)
                if key in obj_map.keys():
                    if flag:
                        obj_map[key] = hex(add(int(obj_map[key], 16),int(map[SymbolName],16)))[2:].zfill(5)
                    else:    
                        obj_map[key] = hex(add(int(obj_map[key], 16),int(map[SymbolName],16)))[2:].zfill(6)[-6:]
                else:    
                    newObjCode = hex(add(int(objCode, 16),int(map[SymbolName],16)) )[2:]
                    if flag:
                        obj_map[key] = newObjCode.zfill(5)
                    else:
                        obj_map[key] = newObjCode.zfill(6)[-6:]
            else:
                if key in obj_map.keys():
                    if flag:
                        obj_map[key] = hex(int(obj_map[key], 16) - int(map[SymbolName],16) & (2**24-1))[2:].zfill(5)
                    else:   
                        obj_map[key] = hex(int(obj_map[key], 16) - int(map[SymbolName],16) & (2**24-1))[2:].zfill(6)[-6:]
                else:    
                    if flag:
                        newObjCode = hex(int(objCode, 16) - int(map[SymbolName],16)  & (2**24-1))[2:].zfill(5)
                        obj_map[key] = newObjCode
                    else:
                        newObjCode = hex(int(objCode, 16) - int(map[SymbolName],16)  & (2**24-1))[2:].zfill(6)
                        newObjCode = newObjCode[-6:]
                        obj_map[key] = newObjCode
            flag = False
            secHead = True
    # modify our memory
    modify(obj_map, df)

    return df
