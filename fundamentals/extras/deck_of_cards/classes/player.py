from . import card
from . import deck

class Player:
    def __init__(self,name):
        self.wins = 0
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.card_info()
            # card.card_points()
        return self

    def point(self):
        for card in self.hand:
            card.card_points()
            return card.card_points()

    def value(self):
        for card in self.hand:
            card.card_value()
        return self

    def draws(self):
        return (deck.deal())


