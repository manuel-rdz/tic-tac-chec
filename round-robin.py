import functools
import os
import shutil

from evaluator import TTCEvaluator

class RoundRobin:
    def __init__(self, players):
        self.players = players
        self.evaluator = TTCEvaluator()
        self.playerStatistics = {}

        self.resultsFolderName = 'results'

        # Fill the default values for statistics
        for player in players:
            self.playerStatistics[player.name] = {
                "won_match": 0,
                "drew_match": 0,
                "lost_match": 0,
                "won_games": 0,
                "drew_games": 0,
                "lost_games": 0,
                "invalid_moves": 0,
                "early_captures": 0,
                "max_captures_exceeded": 0,
                "best_against": "",
                "best_won_games": 0,
                "worst_against": "",
                "worst_won_games": 10000000,
            }
    
    def __fillStatistics(self, stats1, stats2):
        if stats1['wins'] > stats2['wins']:
            self.playerStatistics[stats1['name']]['won_match'] += 1
        elif stats2['wins'] > stats1['wins']:
            self.playerStatistics[stats1['name']]['lost_match'] += 1
        else:
            self.playerStatistics[stats1['name']]['drew_match'] += 1

        self.playersStatistics[stats1['name']]['won_games']+= stats1['wins']
        self.playersStatistics[stats1['name']]['drew_games'] += stats1['draws']
        self.playersStatistics[stats1['name']]['lost_games'] += stats1['loses']

        self.playersStatistics[stats1['name']]['invalid_moves'] += stats1['invalid_moves']
        self.playersStatistics[stats1['name']]['early_captures'] += stats1['early_captures']
        self.playersStatistics[stats1['name']]['max_captures_exceeded'] += stats1['exceed_max_captures']

        if self.playersStatistics[stats1['name']]['best_won_games'] < stats1['wins']:
            self.playersStatistics[stats1['name']]['best_won_games'] = stats1['wins']
            self.playersStatistics[stats1['name']]['best_against'] = stats2['name']

        if self.playersStatistics[stats1['name']]['worst_won_games'] > stats1['wins']:
            self.playersStatistics[stats1['name']]['worst_won_games'] = stats1['wins']
            self.playersStatistics[stats1['name']]['worst_against'] = stats2['name']

    def __compareLeaderBoard(self, a, b):
        for i in len(a):
            if a[i] != b[i]:
                return a[i] > b[i]

    def __createOrEmptyFolder(self, path, folderName):
        folderPath = os.path.join(path, folderName)

        if os.path.exists(folderPath):
            shutil.rmtree(folderPath)

        os.makedirs(folderPath)
        
    def __createLeaderBoard(self):
        leaderboard = []
        for name in self.playerStatistics:
            leaderboard.append((
                name,
                self.playerStatistics[name]['won_match'],
                self.playerStatistics[name]['won_games'],
                self.playerStatistics[name]['drew_match'],
                self.playerStatistics[name]['drew_games']
                ))
            
        leaderboard = sorted(leaderboard, key=functools.cmp_to_key(self.__compareLeaderBoard))
        
        with open(os.path.join(os.getcwd(), 'leaderboard.txt'), 'w') as fp:
            fp.write("Rank (name, won_matches, won_games, drew_matches, drew_games)\n")
            for i in range(5):
                fp.write(str(i + 1) +" "+ str(leaderboard[i]) + "\n")
    
    def __createStatisticsPerPlayer(self):
        folderPath = os.path.join(os.path.join(os.getcwd(), self.resultsFolderName), 'players')
        self.__createOrEmptyFolder(folderPath)

        for name in self.playerStatistics:
            with open(os.path.join(folderPath, name+'.txt'), 'w') as fp:
                    fp.write(str(self.playerStatistics[name]))

    def start(self):
        self.__createOrEmptyFolder(os.getcwd(), self.resultsFolderName)

        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                stats1, stats2 = self.evaluator.runAnalysis(self.players[i], self.players[j], 50, 5, 100)
                self.__fillStatistics(stats1, stats2)
                self.__fillStatistics(stats2, stats1)

        self.__createLeaderBoard()
        self.__createStatisticsPerPlayer()
