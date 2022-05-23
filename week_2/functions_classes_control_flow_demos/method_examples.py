class MethodExamples: 

    def __init__(self):
        self.ez = "I am easily found"


    def get_ez(self):
        return self.ez

    def set_ez(self, value):
        self.ez = value


x = MethodExamples()

print(x.get_ez())
x.set_ez("I have changed")#We can change the value of the class variable for ONLY the instance in this case
print(x.ez)