#James Roth
#5/23/18
#snakeActual.py - snake game for final project

from ggame import *
from random import randint

#constants
CELLSIZE = 20
ROWS = 14
COLUMNS = 20

#colors
green=Color(0x006600,1)
black=Color(0x000000,1)
red=Color(0xff0000,1)
tan=Color(0xd2b48c,1)
white=Color(0xffffff,0)
black=Color(0x000000,1)
blackOutline=LineStyle(1,black)

#functions
def redrawAll(): #clears board
    for item in App().spritelist[:]:
        item.destroy()
    drawSnakeBoard()

def gameOver(): #collided with edge/self - ends game
    print("Game Over")
    data["gameOver"] = 1 #doesn't allow snake to move

def drawSnakeBoard(): #draws background, calls snake creation
    drawSnakeCell()
    Sprite(RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,LineStyle(1,black),white)) #border
    Sprite(TextAsset("Length: " + str(data["lenSnake"]), fill = black, style = "15pt Arial"),(CELLSIZE*COLUMNS+10, 10))

def step(): #runs game
    data["frames"] += 1
    if data["frames"] == 5:
        data["frames"] = 0
        if data["gameOver"] == 0:
            moveSnake(data["movement"][0], data["movement"][1])
        else:
            Sprite(TextAsset("Game Over", fill = red, style = "30pt Arial"),(CELLSIZE*(COLUMNS-4)/2,CELLSIZE*(ROWS-4)/2))

def loadSnakeBoard(): #initial matrix of board
    for i in range(0, ROWS+1):
        list1 = []
        for j in range(0, COLUMNS+1):
            list1.append(0)
        data["board"].append(list1)
    data["board"][data["headY"]][data["headX"]] = 1 #initial snake position
    placeFood()

def drawSnakeCell(): #draws snake and food
    for i in range(0, len(data["board"])):
        for j in range(0, len(data["board"][i])):
            if data["board"][i][j] >= 2:
                Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan),(CELLSIZE*j+1,CELLSIZE*i+1))
            elif data["board"][i][j] == 1:
            Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan),(CELLSIZE*j+1,CELLSIZE*i+1))
                if data["movement"] == [-1,0]:
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.33))
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.67))
                elif data["movement"] == [1,0]:
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.33))
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.67))
                elif data["movement"] == [0,1]:
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.67))
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.67))
                elif data["movement"] == [1,0]:
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.33,(CELLSIZE*i+1)+CELLSIZE*0.33))
                    Sprite(CircleAsset(1,blackOutline,black),((CELLSIZE*j+1)+CELLSIZE*0.67,(CELLSIZE*i+1)+CELLSIZE*0.33))
            elif data["board"][i][j] == -1:
                Sprite(RectangleAsset(CELLSIZE,CELLSIZE,LineStyle(1,black),red),(CELLSIZE*j+1,CELLSIZE*i+1))

def moveUp(event):
    if data["movement"] != [0,1]:
        data["movement"] = [0,-1]

def moveDown(event):
    if data["movement"] != [0,-1]:
        data["movement"] = [0,1]

def moveLeft(event):
    if data["movement"] != [1,0]:
        data["movement"] = [-1,0]

def moveRight(event):
    if data["movement"] != [-1,0]:
        data["movement"] = [1,0]

def moveSnake(col, row): #updates the matrix with the snake's position
    data["headY"] += row
    data["headX"] += col
    if data["board"][data["headY"]][data["headX"]] == -1: #found food?
        data["lenSnake"] += 1
        data["board"][data["headY"]][data["headX"]] = data["lenSnake"]
        placeFood()
    elif data["board"][data["headY"]][data["headX"]] >= 1: #hit yourself?
        gameOver()
    elif data["headY"] >= ROWS or data["headY"] < 0 or data["headX"] >= COLUMNS or data["headX"] < 0: #hit edge?
        gameOver() 
    elif data["board"][data["headY"]][data["headX"]] == 0: #cell empty?
        removeTail()
        data["board"][data["headY"]][data["headX"]] = data["lenSnake"]
    redrawAll()
    
def placeFood(): #places food in the matrix
    Col = randint(0,COLUMNS-1)
    Row = randint(0, ROWS-1)
    if data["board"][Row][Col] == 0:
        data["board"][Row][Col] = -1
    else:
        placeFood()

def removeTail(): #subtracts 1 from every snake cell, removing the end of the snake
    for i in range(0, len(data["board"])):
        for j in range(0, len(data["board"][i])):
            if data["board"][i][j] >= 1:
                data["board"][i][j] -= 1

if __name__ == "__main__":
    #dictionary
    data = {}
    data["board"] = []
    data["gameOver"] = 0
    data["headX"] = COLUMNS/2
    data["headY"] = ROWS/2
    data["lenSnake"] = 1
    data["frames"] = 0
    data["movement"] = [1,0]
    loadSnakeBoard()
    redrawAll()
    
    #arrow controls
    App().listenKeyEvent("keydown","right arrow", moveRight)
    App().listenKeyEvent("keydown","left arrow", moveLeft)
    App().listenKeyEvent("keydown","up arrow", moveUp)
    App().listenKeyEvent("keydown","down arrow", moveDown)
    
    App().run(step)
