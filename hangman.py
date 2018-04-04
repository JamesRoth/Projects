#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *

black=Color(0xffffff,1)
tan=Color(0xf4b642,1)

blackoutline=LineStyle(1, black)

gallows1=RectangleAsset(100,1000,blackoutline,tan)

Sprite(gallows1,(100,100))
App().run()
