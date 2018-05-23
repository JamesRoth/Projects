#James Roth
#5/23/18
#snakeActual.py - snake game for final project

from ggame import *
from random import randint

#constants
CELLSIZE = 20
ROWS = 40
COLUMNS = 26

#colors
green=Color(0x006600,1)
black=Color(0x000000,1)
red=Color(0xff0000,1)
tan=Color(0xd2b48c,1)
blackOutline=LineStyle(1,black)

#functions
def redrawAll(): #clears board
    for item in App().spritelist[:]:
        item.destroy()

def drawSnakeBoard(): #draws bakcground, calls snake creation
    Sprite(RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,blackOutline,green))
    #Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan)) - snake cell

def loadSnakeBoard():
    for i in range(1, ROWS+1)

if __name__ == "__main__":
    #dictionary
    data = {}
    data["board"] = []
    
    
    