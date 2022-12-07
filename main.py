import pandas as pd
from Absolute_Loader import abs_loader
from Linker_Loader import loadMap,modifiedMemory

list = ['Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ,
 'A' , 'B' , 'C' , 'D' , 'E' , 'F' ]

df = pd.DataFrame(columns = list)

# Absolute loader
df = abs_loader.get_absolute_loader(df)
print(df)

# External SymbolTable
headers = ['ControlSection' , 'SymbolName' , 'Address' , 'Length']
df_Loader = pd.DataFrame(columns = headers)
df_Loader = loadMap.getLoadMap(df_Loader)
f = open('generated files\\Ext_Sym_Table.txt', 'w')
dfString = df_Loader.to_string(header = True, index=False)
f.write(dfString)
f.close()

print(df_Loader)
print(loadMap.symbolMap(df_Loader))

# Modified Memory
modifiedMemory.modifyMemory()