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
        return self

    def noise(self):
        print("Woof Woof")
        return self

mr_wiggles = Pet("Mr Wiggles", "Greyhound", "Fetches" )