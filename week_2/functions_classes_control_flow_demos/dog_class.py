class Dog:

    def __init__(self, name, colour):#Here we can initialise variables for an class instance(AKA the constructor)
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()# We can also run functions on initialization

    def bark(self):#Class method. Self refers to the class name
        return "woof"


fido = Dog("fido", "brown")

print(fido.name)
print(fido.colour)