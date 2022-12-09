import pandas as pd
from Absolute_Loader import abs_loader
from Linker_Loader import loadMap,modifiedMemory
from Linker import linker
import pandasgui as pdg
import sys

mem_graph_column = ['Address', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    'A', 'B', 'C', 'D', 'E', 'F']
df = pd.DataFrame(columns=mem_graph_column)

# choose_program = input('This is a loader and linker program!\nPlease choose accordingly [SIC/SICXE]:\n')
# print('here', sys.argv[1])
typeProg = sys.argv[1]

# typeProg = ''
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


# html = df.to_html(classes = 'table design')
# # write html to file
# text_file = open("gui_loader_linker\\index.html", "a")
# text_file.write(html)
# text_file.close()

# pdg.show(df)    
html_str = '''
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SIC/SICXE LOADER-LINKER</title>

    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">  
    <link rel="stylesheet" href="css/style.css">
</head>

<body>
    <div class="main_screen">
        <div class="container">
            <div class="first">
                <div class="attachment">
                    <p style="color:white;">Attach file:</p>
                    <input type="file" name="myfile" id="myfile" style="color: rgb(28, 28, 30);" />
                </div>
            </div>
            <div class="sec">
                <div class="dropdown">
                    <p style="color:white;">Specify:</p>
                    <select name="language" id="language">
                        <option value="SIC">SIC</option>
                        <option value="SICXE">SICXE</option>
                    </select>
                </div>
            </div>
            <div class="col-2">
                <input type="text" id = "address" class="form-control" placeholder="Enter the address" aria-label="Zip">
              </div>
            <div class="third">
                <button id="mybtn">Generate</button>
            </div>
            <div class = "parent">
            {table}
            </div>
            </div>
    </div>
</body>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script type="text/javascript"src="main.js"></script>
</html>
'''

with open("./gui_loader_linker/index.html", "w") as options_f:
    options_f.write(html_str.format(
        table=df.to_html(classes='table design')))