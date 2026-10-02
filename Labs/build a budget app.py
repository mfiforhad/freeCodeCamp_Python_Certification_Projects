class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.get_balance() < amount:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self):
        return sum(b["amount"] for b in self.ledger)

    def transfer(self, amount, other):
        if isinstance(other, Category):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        if amount < self.get_balance():
            return True

    def __str__(self) -> str:
        output = ""
        output += self.name.center(30, "*") + "\n"
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item["amount"]:.2f}"

            output+= f"{description:<23}{amount:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


def create_spend_chart(categories):
    title = "Percentage spent by category"


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
print(food.get_balance())
print(food.withdraw(1600, "restaurant and more food for dessert"))

print(food.get_balance())
print(food.__dict__)
print(food)
