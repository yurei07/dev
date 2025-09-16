import random 
import time
import math
from rich.console import Console

console = Console()

def number(count):
    print('With number?')
    if count == 1:
        return int(input('Number 1: '))
    listOfNumber = []
    for i in range(1,count + 1):
        numbers = int(input(f'Number {i}: '))
        listOfNumber.append(numbers)

    return listOfNumber


def timer():
    rand = random.random()
    value = rand + 2
    time.sleep(value)
    print(value)

def plus(x):
    return  x[0] + x[1]

def minus(x):
    return  x[0] - x[1]

def multiply(x):
    return  x[0] * x[1]

def divide(x): 
    return x[0] / x[1]

def root(x):
    return math.sqrt(x)

def factorial(x): 
    y = 1
    for i in range(2, x + 1):
        y = y * i 
    return y

def subfactorial(num):
    x = 1 
    newList = []
    for i in range(2,num + 1): 
        x = x * i
        newList.append(x)

    final = 0

    for i in range(len(newList) ):
        result = 1 / int(newList[i])
        if i % 2 == 0:
            final = final + result 
        else:
            final = final - result 
    finall = final * newList[-1]
    return finall


while True:
    console.rule('[bold white]Calculator')
    print('1.Plus')
    print('2.Minus')
    print('3.Multiply')
    print('4.Divide')
    print('5.Root')
    print('6.Factorial')
    print('7.Subfactorial')
    try:
        aNumber = int(input('Input a number what do you want to do: '))

        match aNumber:
            case 1:
                print(plus(number(2)))
                timer()
            case 2:
                print(minus(number(2)))
                timer()
            case 3:
                print(multiply(number(2)))
                timer()
            case 4:
                print(divide(number(2)))
                timer()
            case 5:
                print(root(number(1)))
                timer()
            case 6:
                print(factorial(number(1)))
                timer()
            case 7:
                print(subfactorial(number(1)))
                timer()
    except KeyboardInterrupt:
        quit()
            

