class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount=0, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount=0, description=""):
        self.ledger[0].amount -= amount

    def get_balance(self)



def create_spend_chart(categories):
    pass


food = Category("Food")
food.deposit(900, 'deposit')
