
class BingoBoardSquare():
     def __init__(self, text: str, marked:bool, teams: set[int]):
         self.text = text
         self.marked = marked
         self.teams = teams
        
     def isChecked(self, team:int) -> int:
         return self.team.__contains__(team) #get the team number that matches

     def toString(self) -> str:
         string = ""
         string += self.text
         string += f" [{self.marked}]" 
         if not self.teams:
            string += " {'None'}"
         else:
            string += f" {self.teams}"
         return string # return the text on square as a string
     
class BingoBoard():
    def __init__(self, size: int, lockoutBool: bool, squares: list[BingoBoardSquare]):
        self.size = size
        self.lockout = lockoutBool
        if (len(squares) != size * size):
           raise ValueError(f"Size must be EXACTLY {size*size}!\nNumber of squares was {len(squares)}") #ensure the board is the right number of squares
        self.squares = squares
    
    def toString(self) -> str:
       counter = 0
       squareStrings = list()
       #endString = f"\n".join([" ".join(squareStrings[i:i+self.size]) for i in range(0,len(squareStrings),self.size)]) + "\n"
       for i in range(0, len(self.squares)):
           squareStrings.append(f" |{self.squares[i].toString()}| ")
       endString = f"\n".join([" ".join(squareStrings[i:i+self.size]) for i in range(0,len(squareStrings),self.size)]) + "\n"
       return endString



     
     
    
