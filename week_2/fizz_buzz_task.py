def fizzbuzz(a, b):
    for i in range(1,101):
        if i % a == 0 and i % b ==0:
            i = "FizzBuzz"
        elif i % a == 0:
            i = "Fizz"
        elif i % b == 0:
            i = "Buzz"
        print(i)
    return "Done"

print(fizzbuzz(10,2))
