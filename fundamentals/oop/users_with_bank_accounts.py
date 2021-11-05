class User:
    def __init__(self,first_name,last_name):
        self.name = last_name, first_name
        self.account = BankAccount(2, 500)

    def make_deposit(self, amount):
        self.account.deposit += amount

    def make_withdrawl(self, amount):
        self.account.withdraw -= amount

    def display_user_balance(self):
        print(self.name)
        print(self.account.display_account_info)

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

class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        if BankAccount.can_deposit(self.balance,amount):
            self.balance += amount
        return self

    @staticmethod
    def can_deposit(balance, amount):
        if(balance + amount) > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging A $5 fee")
            self.balance -= 5
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True

    def display_account_info(self):
        final = self.balance
        print("Balance: $", final)

    def yield_interest(self):
        if BankAccount.can_yield_interest(self.balance):
            self.balance = ((self.balance * (self.int_rate / 100)) + (self.balance))
        return self

    @staticmethod
    def can_yield_interest(balance):
        if(balance) > 0:
            return True
        else:
            return False

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

BankAccount.print_all_accounts()

savings = BankAccount()
checking = BankAccount()
