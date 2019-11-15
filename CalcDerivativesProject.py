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
listExtreme = []
listPOI = []

#functions
def numDeriv(x,h):
    ans = (f(x+h) - f(x-h))/(2*h)
    return round(ans,3) 
    
def numDerivLeft(x,h): #does derivative at the left endpoint
    ans = (f(x+h) - f(x))/(h)
    return round(ans,3) 

def numDerivRight(x,h): #does derivative at the right endpoint
    ans = (f(x-h) - f(x))/(h)
    return round(ans,3) 

def numSecDeriv(x,h): #finds the second derivative at x
    leftDeriv = numDeriv(x-h, h)
    rightDeriv = numDeriv(x+h,h)
    return round((leftDeriv - rightDeriv)/((2*h)),3) 

def f(x): #the function we are currently finding all the info for
    return x**3

def checkIncDec(listMax,listMin):
    listExtreme = listMax + listMin
    for i in range (0, len(listExtreme)-1):
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) < 0:
                print("Decreasing from ",listExtreme[i],"to ",listExtreme[i + 1])
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) > 0:
                print("Increasing from ",listExtreme[i],"to ",listExtreme[i + 1])
                
def checkIncDec2():
    listExtreme2 = listMax2 + listMin2
    for i in range (0, len(listPOI)):
            if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) < 0:
                print("Concave down from ",listPOI[i],"to ",listPOI[i + 1])
            if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) > 0:
                print("Concave up from ",listPOI[i],"to ",listPOI[i + 1])

def finder(stepDeriv,domainLow,domainHigh): #finds all of the information we want to know, the "master function"
    listMin = []
    listMax = []
    listPOI = []
    x = round(domainLow) #left endpoint case
    val = numDerivLeft(x,tolerance)
    if val > 0:
        listMin.append(domainLow)
        print("happened")
    elif val < 0:
        listMax.append(domainLow)
        print("happened")
    for i in range (1, stepDeriv*abs(domainLow-domainHigh)-1):
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
        if numSecDeriv(x-tolerance, tolerance)*numSecDeriv(x+tolerance,tolerance) < 0:
            print("POI", x)
            listPOI.append(x)
    x = round(domainHigh) #right endpoint case
    val = numDerivRight(x,tolerance)
    if val > 0:
        listMax.append(domainHigh)
        print("happened")
    elif val < 0:
        listMin.append(domainHigh)
        print("happened")
    checkIncDec(listMax,listMin)

def maxFinder():
    largestX = listMax[0]
    for i in range(0,len(listMax)):
        if f(listMax[i]) > f(largestX):
            largestX = listMax[i]
    print('Abs max at x=', largestX)
    
def minFinder():
    smallestX = listMin[0]
    for i in range(0,len(listMin)):
        if f(listMin[i]) > f(smallestX):
            smallestX = listMin[i]
    print('Abs min at x=', smallestX)
    
#print(numDeriv(0,tolerance))
finder(100,-10,10)
print(listMin,listMax)
