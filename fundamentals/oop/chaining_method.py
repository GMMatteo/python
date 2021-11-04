class User:
    def __init__(self,first_name,last_name):
        self.name = last_name, first_name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)
        return self

    def transfer_money(from_account, to_account, amount):
        from_account.make_withdrawl(amount)
        to_account.make_deposit(amount)

GMoney = User("Giacomo", "M")
MontyP = User("Monty", "Python")
SpamA = User("Spam", "Alot")

GMoney.display_user_balance().make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawl(200).display_user_balance()
MontyP.display_user_balance().make_deposit(500).make_deposit(500).make_withdrawl(200).make_withdrawl(200).display_user_balance()
SpamA.display_user_balance().make_deposit(1550).make_withdrawl(500).make_withdrawl(500).make_withdrawl(500).display_user_balance()

User.transfer_money(GMoney, SpamA, 300)

print(GMoney.account_balance)
print(SpamA.account_balance)