import json
from enum import Enum


class MatchStatus(Enum):
    NotRunning = 1
    Starting = 2
    Preparation = 3
    Running = 4
    Finished = 5


class Match():
    def __init__(self):
        self.matchStatus = MatchStatus.NotRunning
        self.ServerTimer = 0
        self.Paused = True
        self.Board : ...
        self.updateMatchStatus()

    def getMatchSeconds(self):
        ...

    def UpdateMatchStatus(self, status: MatchStatus, paused: bool, timer: int, board = None):
        self.ServerTimer = timer
        self.matchStatus = status
        self.Paused = paused
        if(board != None):
            self.Board = board
        self.onMatchStatusChanged()


    def updateMatchStatus(self):
        self.UpdateMatchStatus(self.matchStatus, self.Paused, self.ServerTimer, self.Board)
    
    def onMatchStatusChanged():
        print("onMatchStatusChanged invoked")
    


