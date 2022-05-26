import gc
from excel_generator import *

class Flight_trip:
    def __init__(self, origin, destination, date, passenger_list):
        self.origin = origin 
        self.destination = destination
        self.date = date
        self.passenger_list = passenger_list
        

    def add_passenger(self, f_name, l_name, passport_number):
        self.passenger_list.append([f_name, l_name, passport_number])


    def print_passenger_list(self):
        print(f"List of passengers on flight from {self.origin} to {self.destination} on {self.date}")
        for passenger in self.passenger_list:
            print(passenger)




lon_par = Flight_trip("London", "Paris", "28/04/2022",[])

nyc_tky = Flight_trip("New York", "Tokyo", "28/05/2022",[])

lon_par.add_passenger("Hamza", "Ghazli", 1233453)
lon_par.add_passenger("James", "Smith", 12335543)

nyc_tky.add_passenger("Hamza", "Ghazli", 1233453)

"""
lon_par.print_passenger_list()

nyc_tky.print_passenger_list()


print("List of flights")
for i in gc.get_objects():
    if isinstance(i, Flight_trip):
        print(f" Origin: {i.origin}  Destination: {i.destination} Date: {i.date}")
"""

lon_par_excel = Flight_list_sheet()
lon_par_excel.create_flight_sheet(lon_par.passenger_list)
lon_par_excel.save_file_as("lon_par_passenger_list")