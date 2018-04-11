#James Roth
#4/4/18
#hangman.py - graphics hangman

from ggame import *
from random import randint

def reset(event): #resets game (if it worked)
    word=pickWord
    data["badGuess"]=""
    data["goodGuess"]=""
    data["used"]=""
    data["loss"]=0
    print(data["badGuess"], data["goodGuess"], data["loss"])

def wordComplete(): #checking to see if the whole word is guessed
    if len(data["goodGuess"])==len(word):
        print("You win! Good job.")
        Sprite(TextAsset("You win!",fill=black,style="70pt Arial"),(400,150))
        data["loss"]=2

def guess(event): #when a letter is guessed - is it right or wrong?
    if data["loss"]==0:
        ch=event.key
        if ch not in data["used"]:
            Sprite(TextAsset(ch,fill=black,style="25pt Arial"),(450+25*len(data["used"]),50)) # - drawing letters on top of each other
            data["used"]+=ch
        if ch not in data["badGuess"] and ch not in word:
            data["badGuess"]+=ch
            printHangman(len(data["badGuess"]))
        elif ch in word and ch not in data["goodGuess"]:
            printLetter(word,ch)
        elif ch in data["badGuess"] or ch in data["goodGuess"]:
            print("You've already guessed this letter!")

def printLetter(string,char): #prints a correct letter on the correct line
    i=0
    for ch in string:
        i+=1
        if char==string[i-1]:
            letter=TextAsset(ch,fill=black,style="30pt Arial")
            Sprite(letter,(210+i*70, 460))
            data["goodGuess"]+=ch
    wordComplete()

def printHangman(length): #prints hangman based on incorrect answers
    head=EllipseAsset(30,40,blackoutline,Color(0xfffffff,1))
    body=RectangleAsset(10,90,blackoutline,black)
    arm1=RectangleAsset(50,10,blackoutline,black)
    arm2=RectangleAsset(50,10,blackoutline,black)
    leg1=PolygonAsset([(0,0),(10,0),(60,70),(50,70)],blackoutline,black)
    leg2=PolygonAsset([(0,0),(-10,0),(-60,70),(-50,70)],blackoutline,black)
    for i in range(1,length+1):
        if i==1:
            Sprite(head,(215,100))
        if i==2:
            Sprite(body, (240,180))
        if i==3:
            Sprite(arm1, (190,200))
        if i==4:
            Sprite(arm2, (250,200))
        if i==5:
            Sprite(leg1, (240,270))
        if i==6:
            data["loss"]=1
            Sprite(leg2, (190,270))
            print("You lose! Game over. The word was: " + word)
            Sprite(TextAsset("You lose! The word was: " + word,fill=red,style="30pt Arial"),(400,150))

def pickWord(): #picks a word to use
    num=randint(1,21)
    if num==1:
        return "apocalypse"
    if num==2:
        return "lizard"
    if num==3:
        return "suburban"
    if num==4:
        return "starboard"
    if num==5:
        return "iguana"
    if num==6:
        return "function"
    if num==7:
        return "giraffe"
    if num==8:
        return "abacus"
    if num==9:
        return "radians"
    if num==10:
        return "tornado"  
    if num==11:
        return "hanging"
    if num==12:
        return "blackboard"
    if num==13:
        return "planetary"
    if num==14:
        return "bullfight"
    if num==15:
        return "monkey"
    if num==16:
        return "repiration"
    if num==17:
        return "system"
    if num==18:
        return "computer"
    if num==19:
        return "behest"
    if num==20:
        return "jackhammer"
    if num==21:
        return "rythym"

if __name__ == "__main__":
    
    data={}
    data["badGuess"]=""
    data["goodGuess"]=""
    data["used"]=""
    data["loss"]=0
    
    word=pickWord() 
    
    black=Color(0x000000,1)
    red=Color(0xff0000,1)
    brown=Color(0x934b14,1)
    
    blackoutline=LineStyle(1, black)
    
    gallows1=RectangleAsset(30,500,blackoutline,brown) #makes the gallows
    gallows2=RectangleAsset(240,30,blackoutline,brown)
    gallows3=RectangleAsset(7, 50, blackoutline,black)
    gallows4=PolygonAsset([(0,160),(0,130),(130,0),(160,0)],blackoutline,brown)
    gallows5=RectangleAsset(210,25,blackoutline,brown)
    blank=RectangleAsset(50,7,blackoutline,black)
    
    Sprite(gallows1, (20,50))
    Sprite(gallows2, (40,30))
    Sprite(gallows3, (240,60))
    Sprite(gallows4, (20,30))
    Sprite(gallows5, (0,510))
    for i in range(1,len(word)+1):
        Sprite(blank, (200+i*70, 500))
    
    for ch in "abcdefghijklmnopqrstuvwxyz": #checks for each key pressed
        App().listenKeyEvent("keydown",ch, guess)
    
    #App().listenKeyEvent("keydown","up arrow", reset) #reset doesn't want to work
    
    App().run()