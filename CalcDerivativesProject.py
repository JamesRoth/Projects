#James and Alex Roth
#11/12/19
#Calc derivative project

"""
import scitools.stringfunction
from scitools.StringFunction import StringFunction
f = StringFunction('1+sin(2*x)')
f(1.2)
"""

#delcaring varialbes
tolerance = 0.001
def numDeriv(x,h):
    ((x+h)**2 - (x-h)**2)/(2*h)
    return(round( (((x+h)**2 - (x-h)**2)/(2*h)) ))

print(numDeriv(0,tolerance))
