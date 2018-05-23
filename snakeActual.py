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
    drawSnakeBoard()

def drawSnakeBoard(): #draws background, calls snake creation
    Sprite(RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,blackOutline,green))
    drawSnakeCell()
    #Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan)) - snake cell

def loadSnakeBoard(): #need this current code to only be the initial load, not every time....
    for i in range(1, ROWS+1):
        list1 = []
        for j in range(1, COLUMNS+1):
            list1.append(0)
        data["board"].append(list1)
    data["board"][ROWS/2][COLUMNS/2] = 1 #initial snake position
    placeFood()
    print(data["board"])

def moveSnake(Row, Col):
    while True:
        break
    
def placeFood():
    Col = randint(1,COLUMNS)
    Row = randint(1, ROWS)
    if data["board"][Row][Col] == 0:
        data["board"][Row][Col] = -1

def removeTail():
    for item in data["board"]:
        if 1 in item:
           break 

def findSnakeHead():
    largest = [0,0,0]
    for i in range(0, len(data["board"])):
        for j in range(0, len(data["board"][i])):
            if data["board"][i][j] > largest[2]:
                largest[2] = data["board"][i][j]
                largest[0] = i+1
                largest[1] = j+1

if __name__ == "__main__":
    #dictionary
    data = {}
    data["board"] = []
    loadSnakeBoard()
    
    