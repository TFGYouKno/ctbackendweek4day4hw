class budgetcategory:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum([item["amount"] for item in self.ledger])

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
        total = f"Total: {self.get_balance()}"
        return title + items + total
    
    def display_category_summary(self):
        print(self.__str__())

class budget:
    def __init__(self):
        self.categories = []

    def create_category(self, category):
        self.categories.append(budgetcategory(category))

    def deposit(self, category, amount, description=""):
        for cat in self.categories:
            if cat.category == category:
                cat.deposit(amount, description)
                break

    def withdraw(self, category, amount, description=""):
        for cat in self.categories:
            if cat.category == category:
                cat.withdraw(amount, description)
                break

    def transfer(self, category_from, category_to, amount):
        for cat_from in self.categories:
            if cat_from.category == category_from:
                for cat_to in self.categories:
                    if cat_to.category == category_to:
                        cat_from.transfer(amount, cat_to)
                        break
                break

    def display_budget_summary(self):
        for cat in self.categories:
            cat.display_category_summary()

# Create a budget object

my_budget = budget()

# Create categories

my_budget.create_category("Food")
my_budget.create_category("Clothing")
my_budget.create_category("Entertainment")
my_budget.create_category("Utilities")
my_budget.create_category("Rent")
my_budget.create_category("Emergency Fund")

# Deposit funds into categories

my_budget.deposit("Food", 1000, "Initial deposit")
my_budget.deposit("Clothing", 500, "Initial deposit")
my_budget.deposit("Entertainment", 300, "Initial deposit")
my_budget.deposit("Utilities", 200, "Initial deposit")
my_budget.deposit("Rent", 1000, "Initial deposit")
my_budget.deposit("Emergency Fund", 500, "Initial deposit")

# Withdraw funds from categories

my_budget.withdraw("Food", 100, "Groceries")
my_budget.withdraw("Clothing", 50, "T-shirt")
my_budget.withdraw("Entertainment", 20, "Movie tickets")
my_budget.withdraw("Utilities", 100, "Electric bill")
my_budget.withdraw("Rent", 500, "Monthly rent")
my_budget.withdraw("Emergency Fund", 100, "Medical emergency")

# Transfer funds between categories

my_budget.transfer("Food", "Emergency Fund", 50)
my_budget.transfer("Entertainment", "Emergency Fund", 20)

# Display budget summary

my_budget.display_budget_summary()

#UI to interact with management system

while True:
    print("\nBudget Management System")
    print("1. Deposit funds")
    print("2. Withdraw funds")
    print("3. Transfer funds")
    print("4. Display budget summary")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        category = input("Enter the category: ")
        amount = float(input("Enter the amount to deposit: "))
        description = input("Enter the description (optional): ")
        my_budget.deposit(category, amount, description)

    elif choice == "2":
        category = input("Enter the category: ")
        amount = float(input("Enter the amount to withdraw: "))
        description = input("Enter the description (optional): ")
        my_budget.withdraw(category, amount, description)

    elif choice == "3":
        category_from = input("Enter the category to transfer from: ")
        category_to = input("Enter the category to transfer to: ")
        amount = float(input("Enter the amount to transfer: "))
        my_budget.transfer(category_from, category_to, amount)

    elif choice == "4":
        my_budget.display_budget_summary()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")




