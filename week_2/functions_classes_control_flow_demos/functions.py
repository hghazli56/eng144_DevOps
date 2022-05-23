from typing import Dict, List

#Functions
#Functions are blocks of repeatable code that can take in different parameter instances whenever called

def addition(int1, int2):
    return int1 + int2


twoplusthree = addition(2,3)

print(twoplusthree)

def multi_args(*multiargs):
    for arg in multiargs:
        print(arg)


multi_args(1,2,3,4,5,6,7)

def greeting(name: str):
    print("Hello, my name is " + name)

greeting("Hamza")

def division(num: int, denom: int) -> float: #Here, we can put in expected parameter types along with expected return data type
    return num / denom

print(type(division(1,2)))

names = List[str] = ["Tom", "Dick", "Harry"]
options = Dict[str:bool] = {"subtitles": True, "Audio Description": False}

