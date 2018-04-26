#James Roth
#4/26/18
#snake.py - snake game (not for class)

from ggame import *
from random import randint

#constants
CELLSIZE=20
ROWS=26
COLUMNS=48

#functions
def spriteMain():
    Sprite(background, (5,5))
    spriteApple()
    spriteSnake(data["headX"],data["headY"])

def step():
    for item in App().spritelist[:]:
        item.destroy()
    spriteMain() #seems to create some sort of infinite loop, doesn't let me stop the program - still not clear how ggame works
    

def touchingApple(): #checks for consumption of apple
    if data["headX"]==data["appleX"] and data["headY"]==data["appleY"]: #may have a slight postion problem, cant test now
        data["length"]+=1
        data["lengthChange"]=1

def collision(): #checks for collision with self or wall - current placeholder while I work out mechanics
    while True:
        break

def spriteApple():
    Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,red), (data["appleX"]*CELLSIZE, data["appleY"]*CELLSIZE))

def spriteSnake(headX, headY): #sprites the snake - but snake not showing up
    Sprite(snakeBox, (headX*CELLSIZE, headY*CELLSIZE))
    for i in range (1, int(len(data["snakePos"])/2)): 
        Sprite(snakeBox, (CELLSIZE*data["snakePos"][i*2], CELLSIZE*data["snakePos"][i*2+1]))

def moveApple():
    data["appleX"]=randint(1,ROWS)
    data["appleY"]=randint(1,COLUMNS)
    spriteApple()

def moveDown():
    headMove(0,-1)
    
def moveUp():
    headMove(0,1)
    
def moveLeft():
    headMove(-1,0)
    
def moveRight():
    headMove(1,0)
    
def headMove(rowC, colC): #updates the snake's position
    if data["lengthChange"]==0:
        data["snakePos"].remove(data["snakePos"][1])
        data["snakePos"].remove(data["snakePos"][0])
    else:
        data["lengthChange"]=0
    data["headX"]+=rowC
    data["headY"]+colC
    data["snakePos"].reverse()
    data["snakePos"].append(data["headY"])
    data["snakePos"].append(data["headX"])
    data["snakePos"].reverse()
    touchingApple()
    collision()

if __name__ == "__main__":
    
    #dictionary
    data={}
    data["lengthChange"]=0
    data["appleX"]=randint(1,ROWS)
    data["appleY"]=randint(1,COLUMNS)
    data["headX"]=ROWS/2-3
    data["headY"]=COLUMNS/2
    data["length"]=4
    data["snakePos"]=[ROWS/2-3, COLUMNS/2, ROWS/2-2, COLUMNS/2, ROWS/2-1, COLUMNS/2, ROWS/2, COLUMNS/2] #initial snake position - head is 1st
    
    #colors
    green=Color(0x006600,1)
    black=Color(0x000000,1)
    red=Color(0xff0000,1)
    tan=Color(0xd2b48c,1)
    blackOutline=LineStyle(1,black)

    #assets
    background=RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,blackOutline,green)
    snakeBox=RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan)
    
    #spriting the assets
    spriteMain()
    
    #arrow controls
    App().listenKeyEvent("keydown","right arrow",moveRight)
    App().listenKeyEvent("keydown","left arrow",moveLeft)
    App().listenKeyEvent("keydown","up arrow",moveUp)
    App().listenKeyEvent("keydown","down arrow",moveDown)
    
    App().run()
