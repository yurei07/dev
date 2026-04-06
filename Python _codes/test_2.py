import glob
listFile = []
def find_files(pattern):

     # finding all files matching the pattern
    return glob.glob(pattern, recursive=True)

files = find_files('/home/laptop_Prizrak/MyHobby/Python _codes/test.py')
files1 = find_files('/home/laptop_Prizrak/MyHobby/Python _codes/test_1.py')

for file in files:
    print(file)
    with open(file, 'r') as file:
        content = file.read()
        listFile.append(content)

for file1 in files1:
    with open(file1, 'r') as file1:
        content = file1.read()
        listFile.append(content)
         
j = 0
for i in range(1, len(listFile)):
    if listFile[i] == listFile[j]:
        print('it is the same content')
        break
    else:
        print('it is not the same content')
        break
    j = i
