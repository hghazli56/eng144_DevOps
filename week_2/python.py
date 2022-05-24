from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False #Because pythons do not have venom, we change the value of self.venom from the superclass "Snake" 
    
    def digest_large_prey(self):
        print("I had a big meal")

    def constrict(self):
        print("squeeeze")

    def climb(self):
        print("climb")

    def shed_skin(self):
        print("Out with the old")


