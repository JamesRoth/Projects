#James Roth
#5/23/18
#snakeActual.py - snake game for final project

from ggame import *
from random import randint

#constants
CELLSIZE = 20
ROWS = 28
COLUMNS = 40

#colors
green=Color(0x006600,1)
black=Color(0x000000,1)
red=Color(0xff0000,1)
tan=Color(0xd2b48c,1)
blackOutline=LineStyle(1,black)

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()

spriteAll():
    Sprite(RectangleAsset(CELLSIZE*COLUMNS,CELLSIZE*ROWS,blackOutline,green))
    Sprite(RectangleAsset(CELLSIZE,CELLSIZE,blackOutline,tan))

