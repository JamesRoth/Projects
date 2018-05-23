#James Roth
#5/23/18
#snakeActual.py - snake game for final project

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
