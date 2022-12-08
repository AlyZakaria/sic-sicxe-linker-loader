import pandas as pd
from Absolute_Loader import abs_loader
from Linker_Loader import loadMap,modifiedMemory
from Linker import linker
import pandasgui as pdg


mem_graph_column = ['Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'A', 'B', 'C', 'D', 'E', 'F']
df = pd.DataFrame(columns=mem_graph_column)

choose_program = input('This is a loader and linker program!\nPlease choose accordingly [SIC/SICXE]:\n')
if choose_program.upper() == 'SIC':
    # Absolute loader
    df = abs_loader.get_absolute_loader(df)

elif choose_program.upper() == 'SICXE':
    # Linker
    df = linker.get_linker(df)
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


# html = df.to_html(classes = 'table design')
# # write html to file
# text_file = open("gui_loader_linker\\index.html", "a+")
# text_file.write(html)
# text_file.close()

pdg.show(df)    