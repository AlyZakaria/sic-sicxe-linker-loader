from Linker_Loader import loadMap


def getCell(stAddress, stRec, SymbolName):
    orgAddress = hex(add(stAddress, int(str(stRec),16)))[2:].upper()
    
def modifyMemory(df):
    # print(loadMap.modifiedRec)
    startAddress = df.iloc[0,0]
    for i in loadMap.modifiedRec:
        startRec = i[1:7]
        SymbolName = i[10:]
        # to get the cell & Modify it
        getCell(startAddress, startRec, SymbolName)
    return
