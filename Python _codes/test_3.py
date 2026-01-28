import os 
import pathlib

user = "Prizrak"
userLaptop = "laptop_Prizrak"

pathBathEtc = pathlib.Path('/etc/')
pathBathHome = pathlib.Path(f'/home/{user}/')
pathBathHomeD = pathlib.Path(f'/home/{user}/Documents')

nixos = pathlib.Path('/etc/nixos/modules/tui/neovim/development')
#nixos = pathlib.Path(f'/home/{user}/Documents/nixos/')

newNixos = pathlib.Path(f'/home/{user}/Documents/rhodium/home/development')

# OPEN DIRECTORIES AND FIND FILES
def traverse_directories(current_path: pathlib.Path):
    listFiles = []

    for i in current_path.iterdir():
        if i.is_dir():
            function = traverse_directories(i)
            listFiles.extend(function)
        elif i.is_file():
            if i.suffix == '.nix':
                listFiles.append(i)


    return listFiles

nameNew = traverse_directories(newNixos)
nameOld = traverse_directories(nixos)


for j in range(len(nameNew)):
    for i in range(2, len(nameOld)):
        new = nameNew[j].relative_to(pathBathHome)
        old = nameOld[i].relative_to(pathBathEtc)
        if new == old:
            if nameNew[j].read_text() == nameOld[i].read_text(): 
                print(True)
            elif nameNew[j].read_text() != nameOld[i].read_text():
                print(f'The files arent correct :( : {nameNew[j].read_text()} and {nameOld[i].read_text()}')
                question = input("Do you want to upgrade? (input y/n y = yes, n = no): ")
                if question.lower() == 'y':
                    content = nameNew[j].read_text(encoding='utf-8')
                    nameOld[i].write_text(content, encoding='utf-8')
                    print('IT WORKS!!!!!!!')
                    print(nameNew[j], nameOld[i])
    

