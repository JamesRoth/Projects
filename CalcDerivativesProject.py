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
def NumDeriv(x,h):
    ((x+h)**2 - (x-h)**2)/(2*h)
    print(((x+h)**2 - (x-h)**2)/(2*h))
