foods = [65, 80, 80, 90]


def minimum_percentage(foods):
    perc = 0
    visitors = 0
    min_perce = 0
    
    for i in range(len(foods)):
        perc = perc + foods[i] 
        visitors += 1
    min_perce = max(0,perc  - (visitors - 1)  * 100)
    print(min_perce)

minimum_percentage(foods)

    
