# Что должен делать File Organazier:
#     Сортировать файлы по нужным папкам
#     Поиск 
# Как сортировать?:
#     Он находит все нужные пути и видет файлы в папках в каких не должно лежать те файлы. 
#     Если они там есть то должен проверять файл по окончанию .png .py .exe и закидывать в специальную папку для этого
# Как работает поиск?:
#     Это я буду делать прям потом потом но если буду то можно добавить так что бы при вводи какого либо название то скрипт будт 
#     чекать мои файлы где я храню все и искать по названию. Больше как сверять и выводить что похоже будет на него

import pathlib as pa 
import subprocess as sub

mainPath = pa.Path('/home/Prizrak')
object = []

imagesFile = mainPath.joinpath('Pictures')
docFile = mainPath.joinpath('Documents')
downFile = mainPath.joinpath('Downloads')

imagesSuffix = ['.jpg', '.jpeg', '.jpe', '.jfif', '.png', '.tiff', '.tif', '.webp', '.heic', '.heif', '.gif', '.svg', '.ai']
downSuffix = ['.sh', '.apk', '.pkg', '.exe', '.msi', '.zip', '.7z', '.png', 'rar']

# проверяет суфиксы и переберает папки и элементы в любой дериктории. 
def checkSuffix(suffix, main, objects):
    objects.clear()
    for i in main.iterdir(): # перебирает все элементы в данном пути
        for index, element in enumerate(suffix): # выводит индекс и сам элемент 
            if i.match(f'*{element}'):
                objects.append(i)
            else:
                pass
    # result = sub.run(['ls'], stdout=sub.PIPE, encoding='utf-8')
    # print(result.stdout)


# перемещает файл и определенным суфиксом в другую папку 
def moveFilesInMainFolder(objects, file):
    for i in objects:
        sub.run(['mv', f'{i}', f'{file}'])
                              #выводит инфу о команде; выводит его в норм тексте
    # result = sub.run(['ls', f'{file}'], stdout=sub.PIPE, encoding='utf-8')
    # print(result.stdout)


# это для перемещение файлов в специальные папки 
def moveFilesOfPictures(objects):
    for i in objects:
        match i.suffix:
            case '.png':
                sub.run(['mv', f'{i}', f'{imagesFile.joinpath('png')}'])
            case '.jpg':
                sub.run(['mv', f'{i}', f'{imagesFile.joinpath('jpg')}'])
            case '.jpeg':
                sub.run(['mv', f'{i}', f'{imagesFile.joinpath('jpeg')}'])
        if 'pass' and '.jge' and '.jfif' and '.tiff' and '.webp' and '.heic' and '.gif' and '.svg' and '.ai':
            sub.run(['mv', f'{i}', f'{imagesFile.joinpath('other')}'])

def moveFilesOfDownloads(objects):
    for i in objects:
        match i.suffix:
            case '.zip':
                sub.run(['mv', f'{i}', f'{downFile.joinpath('zip')}'])
            case '.7z':
                sub.run(['mv', f'{i}', f'{downFile.joinpath('7z')}'])
            case '.pdf':
                sub.run(['mv', f'{i}', f'{downFile.joinpath('pdf')}'])
            case '.rar':
                sub.run(['mv', f'{i}', f'{downFile.joinpath('rar')}'])
        if 'pass' and '.sh' and '.apk' and '.pkg' and '.exe' and '.msi':
            sub.run(['mv', f'{i}', f'{downFile.joinpath('other')}'])
        elif 'pass' and '.jpg' and '.png':
            sub.run(['mv', f'{i}', f'{downFile.joinpath('images')}'])


# перекинуть фотки с основной дериктории в Pictures
checkSuffix(imagesSuffix, mainPath, object)
moveFilesInMainFolder(object, imagesFile)

# чекает папки в Pictures и сортирует по суфексам 
checkSuffix(imagesSuffix, imagesFile, object)
moveFilesOfPictures(object)

# чекает папку в Downloads и сортирует по суфексам
checkSuffix(downSuffix, downFile, object)
moveFilesOfDownloads(object)

