class Customer:
    def __init__(self, fname, lname): #self refers to the object within the class
        self.firstname = fname #Attributes can then be added
        self.lastname = lname

    
    def print(self): #Here we have defined a method that will operate on out data
        print(f"Full name: {self.firstname} {self.lastname}") #This method prints the "firstname" and "last name" attributes from Customer

