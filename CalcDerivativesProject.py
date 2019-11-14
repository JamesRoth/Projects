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
listMax = []
listMin = []

#functions
def numDeriv(x,h):
    ((x+h)**2 - (x-h)**2)/(2*h)
    return(round((((x+h)**2 - (x-h)**2)/(2*h)),3))

def extremeFinder(stepDeriv,domainLow,domainHigh):
    for i in range (0, stepDeriv*abs(domainLow-domainHigh)):
        x = round(domainLow+i/stepDeriv,4)
        if numDeriv(x-tolerance, tolerance)*numDeriv(x+tolerance,tolerance) < 0:
            print("Sign change", x)



def maxFinder():
    listMax = []
    print('Abs Max at x=',max(listMax))
    
def minFinder():
    listMin = []
    print('Abs Min at x=',min(listMin))
    
print(numDeriv(0,tolerance))
extremeFinder(100,-10,10)
