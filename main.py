import pandas as pd
from Absolute_Loader import abs_loader
from Linker import linker

mem_graph_column = ['Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'A', 'B', 'C', 'D', 'E', 'F']
df = pd.DataFrame(columns=mem_graph_column)

choose_program = input('This is a loader and linker program!\nPlease choose accordingly [SIC/SICXE]:\n')
if choose_program.upper() == 'SIC':
    # Absolute loader
    df = abs_loader.get_absolute_loader(df)
    print(df)

elif choose_program.upper() == 'SICXE':
    # Linker
    df = linker.get_linker(df)

