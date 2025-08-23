strs = ["a"]

x = ""
my_list = []

for c in range(len(strs)):
    v = strs[c]
    if c != 2:
         print(v[c:c + 1] )

for i in range(len(strs) - 1):
    j = strs[i + 1] 
    x = strs[i]        
    if x[i:1] == j[i:i + 1]:
        my_list.append(x[i:i + 1]) 

    elif x[i:i + 1] != j[i:i + 1]:
        print('')
 
join_list = ''.join(my_list)
print(join_list)
