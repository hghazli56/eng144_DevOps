
secret_animal = "Griffin"

name = input("What is your name? ")
height = input("How tall are you? ")
colour = input("What is your favourite colour? ")
secret_animal_guess = input(f"Enter your secret animal guess. Hint the animal name begins with {secret_animal[0]} and ends with {secret_animal[-1]}. Its name is {len(secret_animal)} letters long:")

print(f"Hello {name}. Your height is {height} and your favourite colour is {colour}")

if secret_animal.lower() == secret_animal_guess.lower():
    print("Well done! you guessed the secret animal!")
else:
    print("Unlucky, you didn't guess the secret animal this time")