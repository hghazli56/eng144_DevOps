from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()#Inherit variables from superclass
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("I will go somewhere warm")

    def hunt(self):
        print("wait, then pounce")

    def use_venom(self):
        print("bite to kill")

    def attract_through_scent(self):
        print("I smell good")

