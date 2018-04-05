#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *
from random import randint

def pickWord():
    num=randint(1,7)
    if num==1:
        return "apocalypse"
    if num==2:
        return "lizard"
    if num==3:
        return "garden"
    if num==4:
        return "starboard"
    if num==5:
        return "iguana"
    if num==6:
        return "function"
    if num==7:
        return "giraffe"

if __name__ == "__main__":
    
    word=pickWord
    
    black=Color(0x000000,1)
    brown=Color(0x934b14,1)
    
    blackoutline=LineStyle(1, black)
    
    gallows1=RectangleAsset(30,1000,blackoutline,brown)
    gallows2=RectangleAsset(240,30,blackoutline,brown)
    gallows3=RectangleAsset(20, 80, blackoutline,black)
    blank=RectangleAsset(70,10,blackoutline,black)
    
    Sprite(gallows1,(20,50))
    Sprite(gallows2, (40,30))
    Sprite(gallows3, (240,60))
    for i in range(1,len(word)+1):
        Sprite(blank, (150+i*100, 600))
    
    
    App().run()
