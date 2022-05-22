class Customer:
    def __init__(self, fname, lname): 
        self._first_name = fname #Adding an underscore before an attribute communicates that it is private and should not be used by other pieces of code
        self._last_name = lname

    
    def print(self): 
        print(f"Full name: {self._first_name} {self._last_name}") 

    @property
    def first_name(self):
        print("In get method")
        return self._first_name #This function retrieves (or gets) an attribute instance from a class(in this case the first name) 

    @first_name.setter
    def first_name(self, new_first_name):
        print("In set method")
        self._first_name = new_first_name #This function processes (or sets) the attribute retrieved from the the getter method

