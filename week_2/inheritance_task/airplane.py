from aircraft import Aircraft

class Airplane(Aircraft):
    def __init__(self, type, make, model, top_speed, number_of_turbines):
        super().__init__(type)
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.number_of_turbines = number_of_turbines
    
    def print_plane_specs(self):
        print(f"Airplane specs: Make:{self.make} Model:{self.model} Top Speed:{self.top_speed} No.of Turbines:{self.number_of_turbines}")



boeing747 = Airplane("airplane", "Boeing", "747", 500, 4)
boeing747.print_plane_specs()



 

        

