#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *

black=Color(0x000000,1)
brown=Color(0x934b14,1)

blackoutline=LineStyle(1, black)

gallows1=RectangleAsset(30,1000,blackoutline,brown)
gallows2=RectangleAsset(240,30,blackoutline,brown)
gallows3=LineAsset(200,200,LineStyle(1,brown))

Sprite(gallows1,(20,50))
Sprite(gallows2, (40,30))
Sprite(gallows3,(200,200)
App().run()
