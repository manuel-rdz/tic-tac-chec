class PlayerWrapper:
    def __init__(self, player, piecesColor):
        self.player = player
        self.captures = 0
        self.pawnDirection = -1
        self.piecesColor = piecesColor

        self.statistics = {
            'name': self.player.name,
            'wins': 0,
            'loses': 0,
            'draws': 0,
            'time_limit_exceeded': 0,
            'raised_errors': 0,
            'invalid_moves': 0,
            'early_movements': 0,
            'exceed_max_captures': 0,
        }

    def resetValues(self, color):
        self.player.reset()
        self.player.setColor(color)
        self.captures = 0
        self.pawnDirection = -1
        self.piecesColor = color