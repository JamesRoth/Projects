#James Roth
#4/26/18
#snake.py - snake game (not for class)

from ggame import *
from random import randint

#constants
CELLSIZE=20
ROWS=28
COLUMNS=52

#functions
def touchingApple():
    

def touchingSelf():
    

def spriteSnake(length): #sprites the snake, takes length as an input so I dont have to type data["length"] every time
    Sprite(snakeBox)

def moveApple():
    data["appleX"]=randint(1,ROWS)
    data["appleY"]=randint(1,COLUMNS)

def moveDown():
    headMove(0,-1)
    
def moveUp():
    headMove(0,1)
    
def moveLeft():
    headMove(-1,0)
    
def moveRight():
    headMove(1,0)
    
def headMove(rowC, colC): #updates the snake's position
    data["snakePos"].remove(data["snakePos"][1])
    data["snakePos"].remove(data["snakePos"][0])
    data["snakePos"].append(data["headX"]+rowC)
    data["snakePos"].append(data["headY"]+colC)
    touchingApple()
    touchingSelf()

if __name__ == "__main__":
    
    #dictionary
    data={}
    data["appleX"]=randint(0,ROWS)
    data["appleY"]=randint(0,COLUMNS)
    data["headX"]=ROWS/2
    data["headY"]=COLUMNS/2
    data["length"]=4
    data["snakePos"]=[ROWS/2-3, COLUMNS/2-3, ROWS/2-2, COLUMNS/2-2, ROWS/2-1, COLUMNS/2-1, ROWS/2, COLUMNS/2] #initial snake position
    
    #colors
    green=Color(0x006600,1)
    black=Color(0xffffff,1)
    red=Color(0xff0000,1)
    tan=Color(0xd2b48c,1)
    blackOutline=LineStyle(1,black)

    #assets
    background=RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,blackOutline,green)
    snakeBox=RectangleAsset(COLUMNS,ROWS,blackOutline,tan)
    
    #spriting the assets
    Sprite(background)
    spriteSnake(data["length"])
    
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    
    App().run(step)
