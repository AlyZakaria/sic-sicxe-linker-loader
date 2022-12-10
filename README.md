# SIC/SICXE Loader_Linker
### Absolute Loader
• An object program is loaded at the
address specified on the START
directive.\
• No relocation or linking is needed
### Program Linking
• A program may be composed of many control sections.\
• These control sections may be assembled separately.\
• These control sections may be loaded at different addresses in
memory.

********************************

## Project Idea
It simulates an [SIC](no control sections only one HTE record) memory for HTE record, and a [SICXE](may have
at least 2 control sections HDRTME records)) memory for HDRTME record with external symbol table.

## Project Criteria
![Input](https://github.com/AlyZakaria/sic-sicxe-linker-loader/blob/main/rsc/photos/Inputs.png)
- whenever you select an input file When selecting the program's type, be sure to specify whether it is a sic or sicxe programm.
- You must enter a start address with four hexadecimal digits when putting a sicxe program.

## How to run the project?
1. You need to install python.
2. Install pandas by running this command

        pip install pandas
3. open the run.bat file and then change and set your python path
![runBat](https://github.com/AlyZakaria/sic-sicxe-linker-loader/blob/main/rsc/photos/runBat.png)
4. put the directory of the project in run.bat file 
![batFile](https://github.com/AlyZakaria/sic-sicxe-linker-loader/blob/main/rsc/photos/path.png)
4. open the project and change the path to the gui_loader_linker.

5. run this command to install the dependencies

        npm install
6. start the server.
        
        npm start

