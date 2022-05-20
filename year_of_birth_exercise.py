from datetime import date


name = input("Name:")
age = int(input("Age:"))
month = int(input("Birth month:"))
day = int(input("Birth day:"))


current_year = int(date.today().year)
current_month = int(date.today().month)
current_day = int(date.today().day)


year_of_birth = current_year - age - ((current_day, current_month) < (day, month)) 

print(f"{name} was born in {year_of_birth}")
