s = '(]'

def isValid(s):
        a = 0

        for i in s: 
            if '(' == i:
                a =+ 1
            elif ')' == i:
                a -= 1
            elif '[' == i:
                a =+ 2
            elif ']' == i:
                a -= 2
            if '{' == i:
                a =+ 3
            elif '}' == i:
                a -= 3
    
            if a > 0:
                return False
            else:
                return True

