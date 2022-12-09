import pandas as pd
from Absolute_Loader import abs_loader
from Linker_Loader import loadMap,modifiedMemory
from Linker import linker
import pandasgui as pdg
from gui_loader_linker import html 
import sys

mem_graph_column = ['Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'A', 'B', 'C', 'D', 'E', 'F']
df = pd.DataFrame(columns=mem_graph_column)


typeProg = sys.argv[1]

if typeProg.upper() == 'SIC':
    # Absolute loader
    df = abs_loader.get_absolute_loader(df)

elif typeProg.upper() == 'SICXE':
    # Linker
    start_address = sys.argv[2]     
    df = linker.get_linker(df, start_address)
    # External SymbolTable
    print(df)
    headers = ['ControlSection' , 'SymbolName' , 'Address' , 'Length']
    df_Loader = pd.DataFrame(columns = headers)
    df_Loader = loadMap.getLoadMap(df_Loader, linker.starting_mem_address)
    f = open('generated files\\Ext_Sym_Table.txt', 'w')
    dfString = df_Loader.to_string(header = True, index=False)
    f.write(dfString)
    f.close()
    
    # Modified Memory
    df = modifiedMemory.modifyMemory(df, df_Loader)



with open("./gui_loader_linker/index.html", "w") as options_f:
    options_f.write(html.html_str.format(
        table=df.to_html(classes='table table-dark table-striped')))