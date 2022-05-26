
class NewBudgetItems():

    def __init__(self):
        self.budget_items = {}

    def add_budget_item(self, item, value):
        self.budget_items[item] = value

    def return_budget_item_value(self, key):
        try:
            return self.budget_items[key]
        except KeyError:
            print("Key was not found")
            raise


    def delete_budget_item(self,item):
        try:
            del self.budget_items[item]
        except KeyError:
            print("key was not found")
            raise

    def print_budget_items(self):
        print(self.budget_items)

    def save_budget_items(self, file_name_and_path ="default"):
        self.create_budget


budget = NewBudgetItems()
budget.add_budget_item("dinner", 10)
budget.print_budget_items()
budget.return_budget_item_value("dinner")