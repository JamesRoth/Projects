#James Roth
#5/23/18
#snakeActual.py - snake game for final project

from ggame import *
from random import randint

#constants
CELLSIZE = 20
ROWS = 24
COLUMNS = 34

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

def loadSnakeBoard(): #initial matrix of board
    for i in range(1, ROWS+1):
        list1 = []
        for j in range(1, COLUMNS+1):
            list1.append(0)
        data["board"].append(list1)
    data["board"][data["headY"]][data["headX"]] = 1 #initial snake position
    placeFood()
    print(data["board"])

def drawSnakeCell(): #draws snake and food
    for i in range(0, len(data["board"])):
        for j in range(0, len(data["board"][i])):
            if data["board"][i][j] >= 1:
                Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan),(CELLSIZE*j+1,CELLSIZE*i+1))
                print("drawn")
            if data["board"][i][j] == -1:
                Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,red),(CELLSIZE*j+1,CELLSIZE*i+1))

def moveUp(event):
    moveSnake(0, -1)

def moveDown(event):
    moveSnake(0, 1)

def moveLeft(event):
    moveSnake(-1, 0)

def moveRight(event):
    moveSnake(1, 0)

def moveSnake(Row, Col): #seems to be creating two more snake parts - but I'm not pressing the arrow keys, the only time its being called?
    data["headY"] += Col
    data["headX"] += Row
    data["board"][data["headY"]][data["headX"]] = data["lenSnake"]
    drawSnakeCell()
    removeTail()
    
def placeFood():
    Col = randint(0,COLUMNS-1)
    Row = randint(0, ROWS-1)
    if data["board"][Row][Col] == 0:
        data["board"][Row][Col] = -1

def removeTail():
    for i in range(0, len(data["board"])):
        for j in range(0, len(data["board"][i])):
            if data["board"][i][j] >= 1:
                data["board"][i][j] -= 1
   

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
    data["headX"] = COLUMNS/2
    data["headY"] = ROWS/2
    data["lenSnake"] = 1
    loadSnakeBoard()
    redrawAll()
    
    #arrow controls
    App().listenKeyEvent("keydown","right arrow", moveRight)
    App().listenKeyEvent("keydown","left arrow", moveLeft)
    App().listenKeyEvent("keydown","up arrow", moveUp)
    App().listenKeyEvent("keydown","down arrow", moveDown)
    
    App().run()
    