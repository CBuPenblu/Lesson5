class Account():

    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Account deposit was successfull. Account balance - {self.balance}$")
    def windraw(self, money):
        if money > self.balance:
            print(f"Not enough funds on your account")
        elif money <= self.balance:
            self.balance -= money
            print(f"Funds windraw of {money}$ was successfull. There is {self.balance}$ left on your account")

    def all_balance(self):
        print(f"Your current balance is {self.balance}$")

man = Account("125", 1000)

man.all_balance()
man.windraw(300)
man.windraw(1000)
man.deposit(2500)