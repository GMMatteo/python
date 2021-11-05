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

savings = BankAccount(.7, 50)
checking = BankAccount(.8, 500)

savings.deposit(500).deposit(500).deposit(500).withdraw(200).yield_interest().display_account_info()
checking.deposit(1500).deposit(2500).withdraw(1200).withdraw(600).withdraw(200).withdraw(200).yield_interest().display_account_info()

BankAccount.print_all_accounts()