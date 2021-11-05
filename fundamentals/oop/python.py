class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def example_method(self):
        self.account.make_deposit(100)
        print(self.account.balance)

# User ()
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
# guido.bank_name = "Dojo Credit Union"
# User.bank_name = "Bank of Dojo"

# guido.name = "Guido"
# monty.name = "Monty"

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)
print(monty.account_balance)


class User1:
    # ! CONSTRUCTION FUNCTION !!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

adrien = User1("Adrien", "Dion", 39)
adrien.greeting()

class User2:
    # ! Class Attribute
    population = 0
    # ! CONSTRUCTION FUNCTION !!! CREATES THE INSTANCE OF AN OBJECT
    def __init__(self,first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.savings = BankAccount(.4, 400)
        User.population += 1

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

    @classmethod
    def user_population(cls):
        print(f"{cls.population} users in the program.")

    @staticmethod
    def validate_age(age):
        is_valid = True
        if age <18:
            is_valid = False
        return is_valid

adrien = User1("Adrien", "Dion", 39)
Benny = User("Benny Bob", "McBob", 39)
Benny = User("Mr. Nibbles", "Pancakes", 39)
adrien.greeting()

# TODO: Calling a class method
User.user_population()

class BankAccount:
# class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def with_draw(self,amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
# class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
# class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
# we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
            return sum
