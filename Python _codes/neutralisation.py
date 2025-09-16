s1 = "-+-+-+"
s2 = "-+-+-+"

def neutralise(s1, s2):
    for i in range(len(s1)):
        if s1[i] == '+' and s2[i] == '+':
            print('+', end='')
        elif s1[i] == '-' and s2[i] == '-':
            print('-', end='')
        else:
            print('0', end='')
            
neutralise(s1,s2)
