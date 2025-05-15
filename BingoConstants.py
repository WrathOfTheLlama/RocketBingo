from dataclasses import dataclass

@dataclass
class Team():
    Index: int
    Name: str

@dataclass
class Color(): # Use RGB values to define colors
    r: int
    g: int
    b: int

@dataclass
class ColorName():
    Color: Color # The values that make up the color
    Name: str # The string name associated with the color


# create a dataclass or class for bingo line


class BingoConstants():
    defaultPort = 4502 # not final number, can be anything
    boardSizeMin = 3
    boardSizeMax = 5

    # define colors
    TeamColors = [
                   ColorName(Color(190, 18, 16), "Red"),
                   ColorName(Color(9, 92, 168), "Blue"),
                   ColorName(Color(5, 149, 15), "Green"),
                   ColorName(Color(205, 128, 4), "Orange"),
                   ColorName(Color(135, 35, 208), "Purple"),
                   ColorName(Color(78, 204, 204), "Cyan"),
                   ColorName(Color(237, 115, 216), "Pink"),
                   ColorName(Color(131, 80, 22), "Brown"),
                   ColorName(Color(215, 195, 0), "Yellow")
                ]
    def GetTeamColor(self, team:int) -> Color:
        if(team < self.TeamColors.__len__): #ensure team number is within range
            return self.TeamColors[team].Color
        return Color(0,0,0) #team number was not within range
    
    def GetTeamName(self, team:int) -> str:
        if(team < self.TeamColors.__len__): #ensure team number is within range
            return self.TeamColors[team].Name + " Team"
        return "Empty" #team number was not within range