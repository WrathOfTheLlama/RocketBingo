#import timeit
#import timer # type: ignore
# import numpy as np # type: ignore
import tkinter as tk
from tkinter import messagebox
from RocketBingoCommon.BingoBoard import BingoBoard, BingoBoardSquare
from RocketBingoCommon.BingoConstants import BingoConstants
from RocketBingoCommon.BingoGameSettings import BingoGameSettings

# initialize some variables that will be passed to BingoBoard() class
boardSize: int = 0
teamNum: int = 0
lockout: bool = False
bingoSquares = list()
goals = list() # where each square goal's string will be stored

# get user input to change above values as desired MAKE SURE TO SANITIZE USER INPUT
print(f"\nSETUP\n" + "-"*40)
while True:
    user_input = input(f"What base size should the board be? ").strip()
    if user_input.isdigit():
        boardSize = int(user_input)
        print("\nYou entered:", boardSize)
        break
    else:
        print("Invalid input! Please enter a valid integer.")
    

for i in range(boardSize * boardSize):
    goals.append(f"goal" + str(i+1))

# randomize the list of square goals (strings) that serve as text
randomGoals = random.sample(goals, len(goals))

# debug print out the goals in table/bingo like order
# print(f"\n".join([" ".join(randomGoals[i:i+boardSize]) for i in range(0,len(randomGoals),boardSize)]) + "\n")

# marked status is false by default, and the set of teams should be empty by default
squareMarked = False
squareMarkedByTeams = set()

# now the list of squares is created, each requiring a text string, a "marked" bool, and a set of integers for what team(s) have marked it
for i in range(0, boardSize * boardSize):
    square = BingoBoardSquare(randomGoals[i], squareMarked, squareMarkedByTeams)
    bingoSquares.append(square)
   # debug print statement below
   # print(square.toString())
    
#for squares in bingoSquares:
#   print(f"\n" + squares.toString())

# to create a BingoBoard, we need the size of the board, game mode bool, and a list of BingoBoardSquare()'s
bingoBoard = BingoBoard(boardSize, lockout, bingoSquares)

#print(f"\n\n LEGEND -> |goal_text [markedStatus] {{'team(s)WhoMarked'}}|\n")
#print(bingoBoard.toString())
