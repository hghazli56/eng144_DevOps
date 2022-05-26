from openpyxl import Workbook

class Flight_list_sheet():
    def __init__(self):
        self.workbook = Workbook()
        self.worksheet1 = self.workbook.active
        self.worksheet1["A1"] = "Name"
        self.worksheet1["B1"] = "Surname"
        self.worksheet1["C1"] = "Passport No."

    def add_values_to_cell(self, cell, value):
       self.worksheet1[cell] = value

    def create_flight_sheet(self, flight_list_list):
        cell_marker =2

        for passenger in flight_list_list:
            self.add_values_to_cell("A" + str(cell_marker), passenger[0])
            self.add_values_to_cell("B" + str(cell_marker), passenger[1])
            self.add_values_to_cell("C" + str(cell_marker), passenger[2])
            cell_marker +=1
    
    def save_file_as(self, name):
        self.workbook.save(name + ".xlsx")

