
from itertools import product
from math import prod


def addition(*args):
    return sum(args)

def division(a,b):
    return a/b

def multiply(*args):
    return prod(args)

def subtract(a,b):
    return a-b


print(addition(1,2,3,4))
print(multiply(1,2,3))
print(division(6,2))
print(subtract(3,4))