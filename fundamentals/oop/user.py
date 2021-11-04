class User:
    def __init__(self,first_name,last_name):
        self.name = last_name, first_name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)

    def transfer_money(from_account, to_account, amount):
        from_account.make_withdrawl(amount)
        to_account.make_deposit(amount)

GMoney = User("Giacomo", "M")
MontyP = User("Monty", "Python")
SpamA = User("Spam", "Alot")

GMoney.display_user_balance()
GMoney.make_deposit(500)
GMoney.make_deposit(500)
GMoney.make_deposit(500)
GMoney.make_withdrawl(200)
GMoney.display_user_balance()
MontyP.display_user_balance()
MontyP.make_deposit(500)
MontyP.make_deposit(500)
MontyP.make_withdrawl(200)
MontyP.make_withdrawl(200)
MontyP.display_user_balance()
SpamA.display_user_balance()
SpamA.make_deposit(1550)
SpamA.make_withdrawl(500)
SpamA.make_withdrawl(500)
SpamA.make_withdrawl(500)
SpamA.display_user_balance()
User.transfer_money(GMoney, SpamA, 300)

print(GMoney.account_balance)
print(SpamA.account_balance)