from budget_items_manager import NewBudgetItems

budget = NewBudgetItems()

budget.add_budget_item("dinner", 30)
budget.add_budget_item("lunch", 20)

budget.save_budget_items()