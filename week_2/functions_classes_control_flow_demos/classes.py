from dog_class import Dog


fido = Dog()
lassie = Dog()

fido.breed = "Bulldog"# Here we can change the variable value for an instance of dog without modifying the base class(instantiation)
lassie.breed = "shiba inu"

print(type(fido))
print(fido.breed)
print(fido.bark())
print(lassie.breed)
