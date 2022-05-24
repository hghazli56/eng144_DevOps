class Dog:

    def __init__(self, name, colour, age):#Here we can initialise variables for an class instance(AKA the constructor)
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.age = age
        self.bark()# We can also run functions on initialization

    def bark(self):#Class method. Self refers to the class name
        return "woof"

    def __str__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old dog"
        else:
            return self.__str__()


fido = Dog("fido", "brown", 5)

print(f"{fido:dog}")