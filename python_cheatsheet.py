#Variables
a = 1 #int by default
b = 3.5 #float by default
c = "Hello World!" #String by default

a = a + 5 #variable values can be overwritten as we go down the code

#User Inputs
a = input("Please enter value for a: ") #Python can take user input, optionally you can display a message within the brackets  
print(a) #You can then print the input value to the console

#Arythmic Operators
a = 1 
b = 2
c = 3

a = a + b #Addition

a = a > b #Checks if a is greater than b 
print(a)

float_num = 1.678
int_num = 4

print (float_num + int_num) #floats and integers can be combined, the output will be a float

#String Manipulation

Single_quotes = 'Hello'
Double_quotes = "Hello again"
Quote_in_quote = "I said \"Hello\"" #If you want to include double quotes in a double quoted string

Hw = "Hello! World"

print(Hw[7:]) #Prints everything after 7th index value
print(Hw[-5:])#Prints everything after the 5th last index value
print(Hw[:5])#Prints every before the 5th index value
print(Hw[0:5])#Prints everything from the 1st index value(0) to before the 5th

print(len(Hw))

White_space = "lots of space at the end             "
print(len(White_space))
print(len(White_space.strip()))# Strip removes leading and trailing empty spaces in a string

Example_text = "Here is alot of text"
print(Example_text.count("text")) # .count counts the number of instances(of text in this example) in a string
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
print(Example_text.replace("alot", "a little")) #This replaces "alot" with "a little"

a = "s"
b = "u"
c = "p"

print(a + b + c)#Strings can be concatenated(there will be no space between said strings)

x = 3
y = 5.4
z = "hello"
print(str(x) + str(y) + z)# Since we can't concatenate numerical values with strings, we cant caste the numerical values into strings allowing for joining

print(f"x is {x}, y is {y}, {z}")# we can directly display variable types with f strings

print(f"x times 2 is {x * 2} and capital z is {z.upper()}")#We can also manipulate variables within f strings

#Rounding decimal numbers

pi = 3.14159265359

print(f"Pi to 3 decimal; places is : {pi:3f}")#We can round a float to a specified number of decimal places 

hi = "HelloWorld!"

print(hi.isalpha())#Checks if string is only alphabetical characters
print(hi.islower())
print(hi.endswith("!"))
print(hi.startswith("H"))

#Booleans

a = True
b = False

print(a == b) #Prints False
print(a !=b)
print(a >=True)

print(True and False) #Applies AND logic
print(False and True)
print(False or True) #Applies OR logic


x = 0
y = 10

print(bool(x)) #Prints boolean value of x as false due to zero value
print(bool(y)) #Anything greater than 0 is TRUE

z = None #Remember: None does not equate False. None is a lack of value while FALSE is still technically a value

#Lists

shopping_list= ["eggs", "bread", "milk", "apples"]#Lists are declared with squared brackets

print(shopping_list[0])#Prints the first item (index 0) from the list

shopping_list[0] = "sugar" #This changes the value of the first item to "sugar"

shopping_list.append("carrots")# We can add items to the end of the list with .append

shopping_list.remove("bread")#Specified items can also removed 

shopping_list.pop()# Removes the last item from the list

mix = [1, 2, 3, "one", "two", "three"]#Lists can also contain multiple data types

print(mix[1:3])
print(mix[-2::])
print(mix[::2])

#Tuples

essentials = ("bread", "eggs", "milk")#Tuples are declared using round brackets. Unlike lists, tuples are immutable meaning values cannot be changed

#Dictionaries

student_1 = {
    "name": "James",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["Data", "SQL", "Python", "Java"]
}

print(student_1["stream"])
print(student_1["completed_lesson_names"][0]) #prints the first index in the list for key "completed_lesson_names"

student_1["completed_lesson_names"] = 5 #The value for a key can be changed

student_1["completed_lesson_names"].remove("Java")#Specified values can be altered

print(student_1.keys())#Prints the keys within a dictionary

#Sets

car_parts = {"body", "chassis", "engine"}
car_parts.add("windows")#Items can be added to sets
print(car_parts)#However, items in a set are ordered randomly

#Frozen Sets

x = frozenset([1, 2, 3, 4])#Frozen sets are sets that are immutable 





















