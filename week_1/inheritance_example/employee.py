import person

class Employee(person.Person):
    def __init__(self, fname, lname, department):
        self._department = department
        super().__init__(fname, lname)

    def print(self):
        super().print() #Here we call the print function from the person superclass
        print(f"Department: {self._department}")
         


james = Employee("james", "smith", "sales")

james.print()