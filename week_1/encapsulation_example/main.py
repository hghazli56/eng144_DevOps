import customer

customer_1 = customer.Customer("Hamza", "Ghazli") 
customer_1.print() 
customer_1.first_name = "Hammy" #The set method is called allowing us to change the first name without directly accessing the __init__ function  
customer_1.print() 