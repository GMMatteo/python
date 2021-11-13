from classes.deck import Deck
from classes.player import Player
"""
This game is play by whomever deals the highest card wins
"""
deck = Deck()
deck.shuffle()

# card = deck.drawCard()
class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.p1.score = 0
        self.p2.score = 0

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
        print('')

    def playing_game(self):
        print('')
        print("Lets Play!")
        print('')
        while len(deck.cards) >= 2:
            p1c = self.p1.draw(deck)
            p2c = self.p2.draw(deck)
            p1p = p1c.showHand()
            p2p = p2c.showHand()
            print('')
            print(len(deck.cards))
            if p1p.point() > p2p.point():
                self.p1.score = self.p1.score + 1
                sum1 = self.p1.score
                self.wins(self.p1.name)
                print(sum1)
                
            else:
                self.p2.score = self.p2.score + 1
                sum2 = self.p2.score
                self.wins(self.p2.name)
                print(sum2)

game = Game()
game.playing_game()
