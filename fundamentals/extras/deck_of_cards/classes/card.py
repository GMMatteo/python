class Card:

    def __init__( self , suit , point_val , string_val ):

        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

# CUSTOM CODE

    def card_points(self):
        # print(self.point_val)
        return(self.point_val)

    def card_value(self):
        print(f"{self.string_val} of {self.suit}")
