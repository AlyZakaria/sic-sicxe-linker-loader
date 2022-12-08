from Absolute_Loader import helper_function as hf
from operator import *
import re

startMem = 4000
modifiedRec = []

def handleHeadRec(list,leng, addressList, df):
    global startMem
    newList = []
    # controlSection
    newList.append(list[0:6])
    #Variable
    newList.append('')
    #Address
    startProg = list[7:13]
    prevLength = int(str(leng[-1]),16)
    address = hex(add(prevLength, int(str(startMem), 16)))[2:].upper()
    startMem = address
    newList.append(address)
    addressList.append(address)
    #length
    length = list[14:]
    newList.append(length)
    leng.append(length)
    return newList


def handleDefRec(list,addressList, df):
    newList = []
    defList = re.findall('............', list)
    for i in defList:
        #ControlSection
        newList.append('')
        newList.append(i[0:6])
        #Address
        st_add = int(str(i[6:]), 16)
        address = hex(add(st_add, int(str(addressList[-1]),16)))[2:].upper()
        newList.append(address)
        #Length
        newList.append('')
        df.loc[len(df)] = newList
        newList = []
    

def insertToSymbolTable(list, df):
    leng = ['0']
    address = []
    for line in list:
        if line[0] == 'H':
            df.loc[len(df)] = handleHeadRec(line[1:], leng, address, df)
        elif line[0] == 'D':
            handleDefRec(line[1:], address, df)
    return df

def getLoadMap(df , starting_mem_address):
    global startMem
    startMem = starting_mem_address
    f = open('rsc\\sicxe.txt', 'r')
    list = []
    global modifiedRec
    # put the head & Definitions of controlSections in list
    for line in f.readlines():
        if line[0] == 'H' or line[0] == 'D':
            list.append(line[:-1])
        if line[0] == 'M':
            modifiedRec.append(line[:-1])
    
    # External Symbol Table
    df = insertToSymbolTable(list, df)
    return df

def symbolMap(df):
    map = {}
    for i in range(len(df)):
        control = df.loc[i, 'ControlSection']
        address = df.loc[i, 'Address']
        sybName = df.loc[i, 'SymbolName']
        if control != '':
            map[control] = address
        elif sybName != '':
            map[sybName] = address
    return map