import customer
import employee
import random

if random.randint(0,1) == 0:
    my_person = customer.Customer("Hamza", "Ghazli", "London") 
    my_person.print() 
else:
    my_person = employee.Employee("John", "Smith", "Sales")
    my_person.print()

#In this example, we have set a condition which calls one of the 2 classes to carry out their set tasks