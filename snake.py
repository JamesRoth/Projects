#James Roth
#4/26/18
#snake.py - snake game (for fun)

from ggame import *
from random import randint

#constants
CELLSIZE=20
ROWS=28
COLUMNS=52

#functions
def moveDown():
    headMove(0,-1)
    
def moveUp():
    headMove(0,1)
    
def moveLeft():
    headMove(1,0)
    
def moveRight():
    headMove(0,-1)
    
def headMove(rowC, colC):
    data["snakePos"].remove(data["snakePos"][-1])
    data["snakePos"].remove(data["snakePos"][-2])

if __name__ == "__main__":
    
    #dictionary
    data={}
    data["length"]=4
    data["snakePos"]=[ROWS/2, COLUMNS/2, ROWS/2-1, COLUMNS/2-1, ROWS/2-2, COLUMNS/2-2, ROWS/2-3, COLUMNS/2-3] #initial snake position
    
    #colors
    green=Color(0x006600,1)
    black=Color(0xffffff,1)
    red=Color(0xff0000,1)
    blackOutline=LineStyle(1,black)

    background=RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,blackOutline,green)
    
    #spriting the assets
    Sprite(background)
    
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    
    App.run(step)
