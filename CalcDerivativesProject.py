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
listXVals = []
listDerivs = []
listMax = []
listMin = []


#functions
def numDeriv(x,h):
    ((x+h)**2 - (x-h)**2)/(2*h)
    return(round( (((x+h)**2 - (x-h)**2)/(2*h)),3 ))

print(numDeriv(0,tolerance))

def listDeriv(stepDeriv,domainLow,domainHigh):
    listXVals = []
    listDerivs = []
    for i in range (0, stepDeriv*abs(domainLow-domainHigh)):
        listXVals.append(round(domainLow+i/stepDeriv,4))
        listDerivs.append(numDeriv(listXVals[i],tolerance))
    print(listXVals)
    print(listDerivs)

listDeriv(1000,-10,10)

def critFinder():
    for i in range (0,length(listDerivs))
        if listDerivs = 0:
            print('Critical Point at',)
            
def maxFinder():
    listMax = []
    print('Abs Max at x=',max(listMax))
    
def minFinder():
    listMin = []
    print('Abs Min at x=',min(listMin))
