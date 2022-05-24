#lambdas are functions that are anonymous. They are not declared using "def" and are not stored. 
#They can take multiple parameters but return one result

addition = lambda num1, num2,: num1 + num2

print(addition(2,2))

savings = [234.00, 555.00, 674.00, 78.00]

bonus = list(map(lambda x: x* 1.1, savings))
print(bonus)