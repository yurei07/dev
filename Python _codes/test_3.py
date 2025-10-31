import os
import glob
import pathlib


user = "Prizrak"
userLaptop = "laptop_Prizrak"

nixos = list(pathlib.Path('/etc/nixos/').iterdir())
punkt = '.'
scam = ''

print(nixos)
for i in range(len(nixos)):
    if punkt in str(nixos[i]):
        print(nixos[i], True)
    else:
        path = list(pathlib.Path(f'{nixos[i]}').iterdir())
        scam = path
        print(str(scam))
        print(nixos[i], False)


## FUNCTION FOR FIND MY FILES
def find_files(pattern):
    return glob.glob(pattern, recursive=True)

## MY PATHS TO FILRS
files = find_files(f'/home/{user}/IT/Python _codes/*.py')
files1 = find_files(f'/home/{user}/IT/Python _codes/*.py')

## FUNCTION TO MAKE A LIST NAMES OF MY FILES
def nameFile(file_paths):
    nameList = []
    for name in file_paths:
        namePath = os.path.basename(name)
        nameList.append(namePath)

    return nameList

## FUNCTION TO OPEN MY FILES BY THE PATH 
def openFile(file_paths):
    contentList = []
    for path in file_paths:
        try:
            with open(path, 'r') as f:
                content = f.read()
                contentList.append(content)
        except Exception as e:
            print(f'I dont find the file: {path}: {e}')

    return contentList
    

old = openFile(files)

new = openFile(files1)

nameOld = nameFile(files)
nameNew = nameFile(files1)


#for j in range(len(nameNew)):
#    for i in range(2, len(nameOld)):
#        if nameNew[j] == nameOld[i]:
#           os.system('') 
#        else:
#            print(nameNew[j], nameOld[i], False)
#            break

