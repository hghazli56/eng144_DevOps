from flight_trip import Flight_trip

class Passenger(Flight_trip):
    def __init__(self, f_name, l_name, passport_number, origin, destination, date, passenger_list):
        super().__init__(origin, destination, date, passenger_list)
        self.f_name = f_name 
        self.l_name = l_name
        self.passport_number = passport_number
    
    def print_flight_info(self):
        print(f"{self.f_name} {self.l_name} : Your flight from {self.origin} to {self.destination} is on {self.date}")

    
hamza = Passenger("Hamza", "Ghazli", 12345, "London", "Paris", "01/01/2022", None)

hamza.print_flight_info()

