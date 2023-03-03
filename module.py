"""
Value code for each piece is as follows:
    - pawn moving away from player = 10 for white, -10 for black
    - pawn moving closer to player =  11 for white, -11 for black
    - bishop =  2 for white, -2 for black
    - knight =  3 for white, -3 for black
    - rook =  4 for white, -4 for black

* Note that if the pawn of the opponent has the 10 or -10 code, that would mean that it is moving
away from the opponent and closer to you. (normal direction)

* Note that if the pawn of the opponent has the 11 or -11 code, that would mean that it is moving
closer to the opponent and away from you. (reverse direction)

"""

class TTCPlayer:
    # valuesCode is a list containing the value code that you must use to represent your pieces over the board. 
    # The sign of the value code will tell you if you are playing as white or black pieces.
    # The values are in the order: pawn, bishop, knight, rook
    def __init__(self, valuesCode):
        pass

    def play(self, world):
        pass