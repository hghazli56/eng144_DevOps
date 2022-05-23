#Control Flow

#if statements
# if statements are used to carry out actions based on whether a condition is met or not 

age = 19
if age >= 18: #Here is the condition. If this condition is met...
    print("You are the correct age to watch this film")#...do this
else:# If the condition is not met...
    print("You are too young to watch this film")#...do this instead


film_rating = "Universal"

if film_rating.lower() == "universal":
    print("Suitable for all age groups")
elif film_rating.lower() == "pg":
    print("Children under 13 must watch with an adult")
elif film_rating.lower() == 18:
    print("adults only!")
else:
    print("Incorrect age rating provided")
#elif statements allow us to include multiple conditions with multiple actions. Note: Consider the order of conditions

#Loops

list_data = [1, 2, 3, 4, 5]
embedded_list = [[1,2,3], [4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2:{"name": "Masha", "money": "$3.66"}, 3:{"name": "Roscoe", "money": "$1.14"}}

for num in list_data:#This will iterate along all items(num) in the list....
    print(num * 2)#...and print each item multiplied by 2

for data in embedded_list:
    print(data)
    for num in data:
        print(num)
#We can use nested loops to run for loops within for loops

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for item in dict_data.values():
    print(item["money"])

for num in list_data:
    if num == 3:
        print("I found 3")
    elif num > 3:
        print("Too far")
    else:
        print("Too soon")

#While loops

x = 0
while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x +=1


user_prompt = True
while user_prompt:
    age = input("What is your age:")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age as a digit")

print(f"Your age is {age}")
#This will continue asking for input until an integer is entered into the input prompt




