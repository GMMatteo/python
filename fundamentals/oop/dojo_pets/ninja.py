from pets import Pet

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

gmoney = Ninja("G", "M", "Doggy Treat", "Kibbles", "Mr Wiggles")

# gmoney.feed().walk().bathe()
# print(Pet.energy)
# print(Pet.health)