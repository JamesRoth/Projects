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
listDeriv = []
listPOI = []

#functions
def numDeriv(x,h): #finds the numerical derivative at a point
    ans = (f(x+h) - f(x-h))/(2*h)
    #return round(ans,3) 
    return ans
    
def numDerivLeft(x,h): #does derivative at the left endpoint
    ans = (f(x+h) - f(x))/(h)
    #return round(ans,3) 
    return ans

def numDerivRight(x,h): #does derivative at the right endpoint
    ans = (f(x-h) - f(x))/(-h) # I added the - to the h and hopefully it'll fix the problem, but we need to find WHY it fixes the problem
    #return round(ans,3) 
    return ans

def numSecDeriv(x,h): #finds the second derivative at x
    leftDeriv = numDeriv(x-h, h)
    rightDeriv = numDeriv(x+h,h)
    #return round((leftDeriv - rightDeriv)/(2*h),3) 
    return (leftDeriv - rightDeriv)/(2*h)

def f(x): #the function we are currently finding all the info for
    return x**3 - (2*x)
    print("Func = " + str(x**3 - (2*x)))

def checkIncDec(listMax,listMin): #finds where the function is increasing and decreasing
    listExtreme = listMax + listMin
    for i in range (0, len(listExtreme)-1):
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) < 0:
                print("Decreasing from",listExtreme[i + 1],"to ",listExtreme[i])
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) > 0:
                print("Increasing from",listExtreme[i + 1],"to ",listExtreme[i])

def checkConcav(listPOI): #finds where the function is concave up/concave down
    for i in range (0, len(listPOI)-1):
        if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) > 0:
            print("Concave down from",listPOI[i],"to ",listPOI[i + 1])
        if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) < 0:
            print("Concave up from",listPOI[i],"to ",listPOI[i + 1])

def finder(stepDeriv,domainLow,domainHigh): #finds all of the information we want to know, the "master function"
    listMin = []
    listMax = []
    listMin2 = []
    listMax2 = []
    listPOI = [] #has endpoints as well as POIs
    listPOI.append(domainLow)
    x = round(domainLow) #left endpoint case
    val = numDerivLeft(x,tolerance) #just using this variable so I only calculate this number once
    if val > 0:
        listMin.append(domainLow)
    elif val < 0:
        listMax.append(domainLow)
    for i in range (1, stepDeriv*abs(domainLow-domainHigh)-1):
        x = (domainLow+i/stepDeriv)
        leftDeriv = numDeriv(x-tolerance, tolerance)
        rightDeriv = numDeriv(x+tolerance,tolerance)
        #print(numDeriv(x,tolerance))
        listDeriv.append(numDeriv(x,tolerance))
        #first derivative stuff
        if numDeriv(x, tolerance)*numDeriv(x+(1/stepDeriv),tolerance) < 0:
            print("Sign change", x)
            if leftDeriv > 0:
                listMax.append(x)
            elif leftDeriv < 0:
                listMin.append(x)
        #second derivative stuff
        if numSecDeriv(x, tolerance)*numSecDeriv(x+(1/stepDeriv),tolerance) < 0:
            listPOI.append(x)
            print("POI at ",x)
    x = round(domainHigh) #right endpoint case
    val = numDerivRight(x,tolerance) #just using this variable so I only calculate this number once
    if val > 0:
        listMax.append(domainHigh)
    elif val < 0:
        listMin.append(domainHigh)
    listPOI.append(domainHigh)
    checkIncDec(listMax,listMin)
    print("Maxes at x =",listMax)
    print("Mins at x =",listMin)
    absMaxFinder(listMax)
    absMinFinder(listMin)
    checkConcav(listPOI)
    print(listDeriv)

def absMaxFinder(listMax): #finds the absolute minimum in a list of all minimums
    if len(listMax) > 0:
        if len(listMax) == 1:
            print('Abs max at x =', listMax[0])
        else:
            largestX = listMax[0]
            for i in range(0,len(listMax)):
                if f(listMax[i]) > f(largestX):
                    largestX = listMax[i]
            print('Abs max at x =', largestX)
    
def absMinFinder(listMin): #finds the absolute minimum in a list of all minimums
    if len(listMin) > 0:
        if len(listMin) == 1:
            print('Abs min at x =', listMin[0])
        else:
            smallestX = listMin[0]
            for i in range(0,len(listMin)):
                if f(listMin[i]) < f(smallestX):
                    smallestX = listMin[i]
            print('Abs min at x =', smallestX)


finder(100,-2,2)
#print(numDerivRight(10,tolerance))
