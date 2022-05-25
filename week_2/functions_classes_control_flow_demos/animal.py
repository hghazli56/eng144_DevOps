class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breath(self):
        print("In and out")
    
    def eat(self):
        print("Yummy")
    
    def procreate(self):
        print("lets find a mate")

    def move(self):
        print("walk")

cat = Animal()
