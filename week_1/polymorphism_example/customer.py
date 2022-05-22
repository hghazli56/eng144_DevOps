import person

class Customer(person.Person): # Here we define Customer as a subclass of the Person class 
    def __init__(self, fname, lname, address): #Address is the attribute specific to customer
        self._address = address
        super().__init__(fname, lname) #We initialise the general attributes from the superclass

    def print(self):
        print(f"Address: {self._address}", end = " ")
        super().print() #Here we call the print function from the person superclass 


