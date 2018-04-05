#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *
from random import randint

def guess(event):
    print(event.key)
    print(len(["badGuess"]))
    ch=event.key
    if ch not in ["badGuess"] and ch not in word:
        ["badGuess"]+=ch
        printHangman(len(["badGuess"]))
    if ch in word:
        printLetter(ch)

def printLetter(string):
    i=0
    for ch in string:
        i+=1
        if ch==string[i-1]:
            letter=TextAsset(ch,fill=black,style="italic 30pt Times")
            Sprite(letter,(210+i*70, 460))

def printHangman(length):
    head=EllipseAsset(30,50,blackoutline,Color(0xfffffff,1))
    body=RectangleAsset(10,60,blackoutline,black)
    arm1=RectangleAsset(50,10,blackoutline,black)
    arm2=RectangleAsset(50,10,blackoutline,black)
    leg1=PolygonAsset([(0,0),(10,0),(50,70),(60,70)],blackoutline,black)
    leg2=PolygonAsset([(0,0),(-10,0),(-50,70),(-60,70)],blackoutline,black)
    for i in range(1,length+1):
        if i==1:
            Sprite(head,(215,100))
        if i==2:
            Sprite(body, (215,140))
        if i==3:
            Sprite(arm1, (165,170))
        if i==4:
            Sprite(arm2, (265,170))
        if i==5:
            Sprite(leg1, (215,200))
        if i==6:
            Sprite(leg2, (215,200))

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
    
    data={}
    data["badGuess"]=""
    
    word=pickWord()
    print(word)
    
    black=Color(0x000000,1)
    brown=Color(0x934b14,1)
    
    blackoutline=LineStyle(1, black)
    
    gallows1=RectangleAsset(30,1000,blackoutline,brown)
    gallows2=RectangleAsset(240,30,blackoutline,brown)
    gallows3=RectangleAsset(10, 50, blackoutline,black)
    blank=RectangleAsset(50,7,blackoutline,black)
    
    Sprite(gallows1,(20,50))
    Sprite(gallows2, (40,30))
    Sprite(gallows3, (240,60))
    for i in range(1,len(word)+1):
        Sprite(blank, (200+i*70, 500))
    
    for ch in "abcdefghijklmnopqrstuvwxyz":
        App().listenKeyEvent("keydown",ch, guess)
    
    App().run()