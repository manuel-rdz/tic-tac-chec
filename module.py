"""
Value code for each piece is as follows:
    - pawn = 1 for white, -1 for black
    - bishop =  3 for white, -3 for black
    - knight =  4 for white, -4 for black
    - rook =  5 for white, -5 for black

* It is recommended to store the direction of movement of both your pawn and opponent's pawn.

"""

class TTCPlayer:
    # valuesCode is a list containing the value code that you must use to represent your pieces over the board. 
    # The sign of the value code will tell you if you are playing as white or black pieces.
    # The values are in the order: pawn, bishop, knight, rook
    def __init__(self, valuesCode):
        self.name = "Juanito"

    def play(self, world):
        pass