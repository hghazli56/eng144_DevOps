class Balance:

    def __init__(self, money):
        self.money = money

    def __format__(self, f_spec):
        if f_spec == "inpounds":
            return f"You have £{self.money:.2f}"
        elif f_spec == "inpence":
            return f"You have {self.money * 100:.0f} pence"

hamzabal = Balance(10.3456432)

print(f"{hamzabal:inpounds}")
print(f"{hamzabal:inpence}")


