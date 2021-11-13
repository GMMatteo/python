import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = random.randint(1,15)
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def status(self):
        self.character = "pirate"
        return(self.character)

    def health_stat(self):
        # print(self.health)
        return(self.health)

    def power(self):
        # print(self.strength)
        return(self.strength)