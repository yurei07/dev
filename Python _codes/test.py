#star = '*'
#n = int(input('Width: '))
#n2 = int(input('How many: '))
#
#if n // 2 == 0 or 5 >= n:
#    print('you cant type even number')
#    quit()
#
#for width in range(n ):   
#    if width == 0:
#        print(n * star)
#    elif n // 2 == width :
#        print(n * star)
#    elif n - 1 == width:
#        print(n * star)
#    else:
#        space = n - (width + 1)
#        print(' ' * space + star)

width = int(input('Width: '))
amount = int(input('Amount: '))
step = width - width // 2 - 2
if width % 2 == 1:
    print('type an odd number, not even')
    quit()

def line(length:int, count:int, spaces:int):
    if spaces != 0:
        for _ in range(spaces):
            print(' ', end='')
    for _ in range(length):
        print('*', end='')

def middle(spaces:int, is_double:bool, width:int):
    if is_double:
        width_local = width // 2 - 1
        spaces_local = width // 2 * 3 + 1
        for i in range(width_local - 1):
            if spaces != 0:
                for k in range(spaces):
                    print(' ')
            for _ in range(width_local - i):
                print(' ', end='')
            print('*', end = '')
            for _ in range(spaces_local):
                print(" ", end = '')
            print('*')
    else:
        width_local = width // 2 - 1
        for i in range(width_local - 1):
            if spaces != 0:
                for k in range(spaces):
                    print(' ')
            for _ in range(width_local - i):
                print(' ', end='')
            print('*')

for i in range( amount):
    spaces_local = width * i + 1
    if i == 0: # first Z
        line(width,1,0)
        middle(3,False, width)
        line(width, 2, 0 )
        middle(0, True, width)
        line(width, 3, 0)
    elif i == amount - 1: #last Z
        middle(spaces_local, False, width)
        line(width, 1, spaces_local)
    elif i == amount - 2:
        middle(spaces_local, True, width)
        line(width,2,spaces_local)
    else: #almost last Z
        middle(spaces_local,True,width)
        line(width,3, spaces_local)

