from openpyxl import Workbook

class BudgetExcelGenerator:

    def __init__(self):
        self.workbook = Workbook()
        self.worksheet1 = self.workbook.active
        self.worksheet1["A1"] = "Item"
        self.worksheet1["B1"] = "Value"

    def _add_values_to_cell(self, cell, value):
        self.worksheet1[cell] = value

    def _create_budget_list(self, budget_item_dict):

        cell_marker = 2#Start on row 2 as row 1 has been populated

        for item_key in budget_item_dict:
            value = budget_item_dict.get(item_key)

            self._add_values_to_cell("A" + str(cell_marker), item_key)# Increment up cell as data is populated
            self._add_values_to_cell("B" + str(cell_marker), value)
            cell_marker += 1

    def _save_file_as(self, name):
        self.workbook.save(name + ".xlsx")

"""
excel_gen = BudgetExcelGenerator()
budget_items = {"book": 5.00, "games": 20, "food": 30}
excel_gen._create_budget_list(budget_items)
excel_gen._save_file_as("default")
"""