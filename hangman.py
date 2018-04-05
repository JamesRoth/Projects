#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *
from random import randint

badGuess=""
def guess(event):
    print(event.key)
    ch=event.key
    if ch not in badGuess:
        badGuess+=ch
        printHangman(len(badGuess))

def printHangman(length):
    head=ElipseAsset(100,50,blackoutline,Color(0x000000,1))
    body=RectangleAsset(10,50,blackoutline,black)
    arm1=RectangleAsset(50,10,blackoutline,black)
    arm2=RectangleAsset(50,10,blackoutline,black)
    leg1=PolygonAsset([(0,0),(10,0),(50,70),(60,70)],blackoutline,black)
    leg2=PolygonAsset([(0,0),(-10,0),(-50,70),(-60,70)],blackoutline,black)
    for i in range(1,length+1):
        if i==1:
            sprite=head
        if i==2:
            sprite=body
        if i==3:
            sprite=arm1
        if i==4:
            sprite=arm2
        if i==5:
            sprite=leg1
        if i==6:
            sprite=leg2
        Sprite(sprite)

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
    
    word=pickWord()
    
    black=Color(0x000000,1)
    brown=Color(0x934b14,1)
    
    blackoutline=LineStyle(1, black)
    
    gallows1=RectangleAsset(30,1000,blackoutline,brown)
    gallows2=RectangleAsset(240,30,blackoutline,brown)
    gallows3=RectangleAsset(20, 80, blackoutline,black)
    blank=RectangleAsset(50,7,blackoutline,black)
    
    Sprite(gallows1,(20,50))
    Sprite(gallows2, (40,30))
    Sprite(gallows3, (240,60))
    for i in range(1,len(word)+1):
        Sprite(blank, (200+i*70, 500))
    
    for ch in "abcdefghijklmnopqrstuvwxyz":
        App().listenKeyEvent("keydown",ch, guess)
    
    App().run()
