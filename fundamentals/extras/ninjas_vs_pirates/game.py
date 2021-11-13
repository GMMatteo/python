from classes.ninja import Ninja
from classes.pirate import Pirate
import random

class Game:
        def __init__(self):
            name1 = input("p1 name ")
            name2 = input("p2 name ")
            self.p1 = Ninja("Ninja " + name1)
            self.p2 = Pirate("Pirate " + name2)

        def playing_game(self):
            print('')
            print("Lets Go!")
            print('')
            playerList = [self.p1.status(), self.p2.status()]
            while self.p1.health_stat() >= 0:
                if random.choice(playerList) == "ninja":
                    print(self.p1.name + " Health Is At " + str(self.p1.health_stat()))
                    print(self.p2.name + " Health Is At " + str(self.p2.health_stat()))
                    print('')
                    print("Next Battle " + self.p1.name + " Attacks " + self.p2.name)
                    self.p1.attack(self.p2)
                    print(self.p1.name + " Hits Back With A Force Of " + str(self.p1.power()))
                    print('')
                else:
                    print(self.p2.name + " Health Is At " + str(self.p2.health_stat()))
                    print(self.p1.name + " Health Is At " + str(self.p1.health_stat()))
                    print('')
                    print("Next Battle " + self.p2.name + " Attacks " + self.p1.name)
                    self.p2.attack(self.p1)
                    print(self.p2.name + " Hits Back With A Force Of " + str(self.p2.power()))
                    print('')
                if self.p1.health_stat() <= 0:
                    self.p2.show_stats()
                    self.p1.show_stats()
                    print(self.p2.name + " You Are Victorious. You Have Defeated " + self.p1.name)
                    print('')
                    break
                if self.p2.health_stat() <= 0:
                    self.p1.show_stats()
                    self.p2.show_stats()
                    print(self.p1.name + " You Are Victorious. You Have Defeated " + self.p2.name)
                    print('')
                    break

game = Game()
game.playing_game()

# mike = Ninja("Michelanglo")

# jack = Pirate("Jack Sparrow")

# mike.attack(jack)
# jack.show_stats()

# jack.attack(mike)
# mike.show_stats()

# jack.health_stat()
# mike.health_stat()

# mike = Ninja("Michelanglo")
# jack = Pirate("Jack Sparrow")
# p1 = mike
# p2 = jack