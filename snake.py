#James Roth
#4/26/18
#snake.py - snake game (for fun)

from ggame import *
from random import randint

CELLSIZE=20
ROWS=28
COLUMNS=52

green=Color(0x006600,1)
black=Color(0xffffff,1)
red=Color(0xff0000,1)
blackOutline=LineStyle(1,black)

if __name__ == "__main__":
    background=RectangleAsset(1000,700,blackOutline,green)
