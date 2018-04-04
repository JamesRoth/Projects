#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *

black=Color(0x000000,1)
brown=Color(0x934b14,1)

blackoutline=LineStyle(1, black)

gallows1=RectangleAsset(30,1000,blackoutline,brown)
gallows2=RectangleAsset(200,30,blackoutline,brown)

Sprite(gallows1,(20,50))
Sprite(gallows2, (40,30))
App().run()
