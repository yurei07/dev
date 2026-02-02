width = int(input("width:"))
if width % 2 != 1:
    print("type an odd number, not even")
    quit()
for i in range(1, width + 1):
    if i == 1 or i == width or i == (width - width // 2):
        for _ in range(width):
            print("*", end="")
        print()
    else:
        for _ in range(width - i):
            print(" ", end="")
        print("*")
