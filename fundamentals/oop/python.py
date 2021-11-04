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

class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

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

