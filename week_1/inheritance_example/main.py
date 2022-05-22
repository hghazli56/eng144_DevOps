import customer
import employee

#In this example, we have moved the firstname and last name attributes to a new superclass(person)
#Both customer and employee inherit firstname and last name from person making them Subclasses of person
#Therefore we can assign attributes from person to customer and employee
customer_1 = customer.Customer("Hamza", "Ghazli", "London") 
customer_1.first_name = "Hammy" 
customer_1.print() 

employee_1 = employee.Employee("John", "Smith", "Sales")
employee_1.print()