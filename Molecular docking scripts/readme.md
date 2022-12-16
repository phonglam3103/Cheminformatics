This is where I post the shell script used to virtual screening using Autodock Vina 1.2.0 and Autodock Vina 1.1.2.
## Pre-requisite: 
1. Windows: Bash.exe (could be installed using cygwin64 at https://www.cygwin.com/)
2. Linux: Do not need any further installation
3. Set up path to the bash.exe (Default C:\cygwin64\bin) (How to set up path? -https://www.mathworks.com/matlabcentral/answers/94933-how-do-i-edit-my-system-path-in-windows)

## Folder requirements
1. protein.pdbqt
2. Multiple ligand files (.pdbqt), could be converted from .mol2 or .pdb using Openbabel
3. Config file (conf.txt_

## Virtual screening using the shell scripts
1. Place the vina.exe in the same directory that consists of the "protein.pdbqt", multiple ligands.pdbqt and conf.txt
2. In the address bar: type cmd
3. _bash vina_screen_local.sh_
4. In the *out* sub-folder, download the vina_screen_get_top.py from this repository, run this code by cmd:
_python vina_screen_get_top.py_
