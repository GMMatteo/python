class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet

    def walk(self):
        self.pet.play(Pet)
        return self

    def feed(self):
        self.pet.eat(Pet)
        return self

    def bathe(self):
        self.pet.noise(Pet)
        return self

class Pet:
    health = 50
    energy = 500
    # implement __init__( first_name , last_name , treats , pet_food , pet )

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    def noise(self):
        print("Woof Woof")
        return self

gmoney = Ninja("G", "M", "Doggy Treat", "Kibbles", "Mr Wiggles")
mr_wiggles = Pet("Mr Wiggles", "Greyhound", "Fetches" )

gmoney.feed().walk().bathe()
print(Pet.energy)
print(Pet.health)

# print(Ninja)