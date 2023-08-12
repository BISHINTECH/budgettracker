import json

def create_budget():
  """Creates a new budget."""
  budget = {}
  budget["income"] = 0
  budget["expenses"] = {}
  return budget

def add_income(budget, amount):
  """Adds income to the budget."""
  amount = int(amount)
  budget["income"] += amount

def add_expense(budget, category, amount):
  """Adds an expense to the budget."""
  amount = int(amount)
  if category not in budget["expenses"]:
    budget["expenses"][category] = 0
  budget["expenses"][category] += amount


def get_budget(filename):
  """Gets the budget from a file."""
  with open(filename, "r") as f:
    budget = json.load(f)
  return budget

def save_budget(budget, filename):
  """Saves the budget to a file."""
  with open(filename, "w") as f:
    json.dump(budget, f)

def main():
  """The main function."""
  budget = create_budget()
  while True:
    print("Budget Tracker")
    print("1. Add income")
    print("2. Add expense")
    print("3. See budget")
    print("4. Save budget")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      amount = input("Enter the amount of income: ")
      add_income(budget, amount)
    elif choice == "2":
      category = input("Enter the expense category: ")
      amount = input("Enter the amount of expense: ")
      add_expense(budget, category, amount)
    elif choice == "3":
      print("Income:", budget["income"])
      for category, amount in budget["expenses"].items():
        print(category, ":", amount)
    elif choice == "4":
      filename = input("Enter the budget file name: ")
      save_budget(budget, filename)
    elif choice == "5":
      break

if __name__ == "__main__":
  main()
