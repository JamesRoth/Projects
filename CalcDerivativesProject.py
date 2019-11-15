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

#functions (numDeriv still only running for x^2)
def numDeriv(x,h):
    ans = (f(x+h) - f(x-h))/(2*h)
    return(round(ans,3))
    
def numDerivLeft(x,h):
    ans = (f(x+h) - f(x))/(h)
    return(round(ans,3))

def numDerivRight(x,h):
    ans = (f(x-h) - f(x))/(h)
    return(round(ans),3))
    
def f(x):
    return x**2
    
def finder(stepDeriv,domainLow,domainHigh): #STILL NEED ENPOINT CASE
    listMin = []
    listMax = []
    for i in range (0, stepDeriv*abs(domainLow-domainHigh)):
        x = round(domainLow+i/stepDeriv,4)
        leftDeriv = numDeriv(x-tolerance, tolerance)
        rightDeriv = numDeriv(x+tolerance,tolerance)
        #first derivative stuff
        if numDeriv(x-tolerance, tolerance)*numDeriv(x+tolerance,tolerance) < 0:
            print("Sign change", x)
            if leftDeriv > 0:
                listMax.append(x)
            elif leftDeriv < 0:
                listMin.append(x)
        #second derivative stuff
        secondDeriv = round((leftDeriv - rightDeriv)/((x+tolerance)-(x-tolerance)),3) #finding the second derivative at x
        
def maxFinder():
    largestX = listMax[0]
    for i in range(0,len(listMax)):
        if listMax[i]**2 > largestX**2:
            largestX = listMax[i]
    print('Abs max at x=', largestX)
    
def minFinder():
    smallestX = listMin[0]
    for i in range(0,len(listMin)):
        if listMin[i]**2 > smallestX**2:
            smallestX = listMin[i]
    print('Abs min at x=', smallestX)
    
print(numDeriv(0,tolerance))
finder(100,-10,10)

if numDerivLeft > 0 and x == domainLow:
    listMin.append(domainLow)
if numDerivLeft < 0 and x == domainLow:
    listMax.append(domainLow)
if numDerivRight > 0 and x == domainHigh:
    listMin.append(domainHigh)
if numDerivRight < 0 and x == domainHigh:
    listMax.append(domainHigh)


