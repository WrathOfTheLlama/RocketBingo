
class BingoBoardSquare():
     def __init__(self, text: str, marked:bool, team: list[int]):
         self.text = text
         self.marked = marked
         self.team = team
        
     def isChecked(self, team:int) -> int:
         return self.team.__contains__(team) #get the team number that matches

     def toString(self) -> str:
         return self.text # return the text on square as a string
     
class BingoBoard():
    def __init__(self, size: int, lockoutBool: bool, squares: list[BingoBoardSquare]):
        self.size = size
        self.lockout = lockoutBool
        if (squares.Length != size * size):
           raise ValueError(f"Size must be EXACTLY {size*size}!") #ensure the board is the right number of squares
        self.squares = squares



     
     
    
