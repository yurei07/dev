word = 'bus'

def pluralize(word): 
    sin_ends = ['s','x','z','ch','sh']
    sin_ends1 = ['ch','sh']
    sin_ends2 = ['y']
    sin_ends3 = ['iy','uy','ay','ey','oy']
    result = ''
    
    for a in range(len(sin_ends)):
        if sin_ends[a] == word[-1:]:
            result = word + 'es'
    for i in range(len(sin_ends1)):
        if sin_ends1[i] == word[-2:]:
            result = word + 'es'
    for j in range(len(sin_ends2)):
        if sin_ends2[j] == word[-1:]:
            result = word[:-1] + 'ies'
    for n in range(len(sin_ends3)):
        if result == '' or sin_ends3[n] == word[-2:]:
            result = word + 's'

    print(result) 

pluralize(word)
