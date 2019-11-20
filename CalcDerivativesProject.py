#James and Alex Roth
#11/12/19
#Calc derivative project

#imports
import math
from math import sin,cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2
from math import ceil, floor

#delcaring varialbes
tolerance = 0.001
listMax = []
listMin = []
listDeriv = []
listPOI = []

#functions
def f(xVal): #the function we are currently finding all the info for
    x=xVal
    return(eval(func))
    #return (x**3) - (2*x)
    #return x**2

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

def checkIncDec(listMax,listMin): #finds where the function is increasing and decreasing
    listExtreme = listMax + listMin
    listExtreme.sort()
    for i in range (0, len(listExtreme)-1):
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) < 0:
                print("Decreasing from",listExtreme[i],"to ",listExtreme[i + 1])
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) > 0:
                print("Increasing from",listExtreme[i],"to ",listExtreme[i + 1])

def checkConcav(listPOI): #finds where the function is concave up/concave down
    listPOI.sort()
    for i in range (0, len(listPOI)-1):
        if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) > 0:
            print("Concave down from",listPOI[i],"to ",listPOI[i + 1])
        if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) < 0:
            print("Concave up from",listPOI[i],"to ",listPOI[i + 1])

def finder(stepDeriv,domainLow,domainHigh): #finds all of the information we want to know, the "master function"
    listMin = []
    listMax = []
    listPOI = [] #has endpoints as well as POIs
    listPOI.append(domainLow)
    x = domainLow #left endpoint case
    val = numDerivLeft(x,tolerance) #just using this variable so I only calculate this number once
    if val > 0:
        listMin.append(domainLow)
    elif val < 0:
        listMax.append(domainLow)
    for i in range (1, stepDeriv*abs(domainLow-domainHigh)-1):
        x = (domainLow+i/stepDeriv)
        leftDeriv = round(numDeriv(x-(1/stepDeriv), tolerance),10)
        rightDeriv = round(numDeriv(x+(1/stepDeriv),tolerance),10)
        deriv = round(numDeriv(x,tolerance),10)
        listDeriv.append(numDeriv(x,tolerance))
        #first derivative stuff
        if deriv*rightDeriv < 0 and deriv != 0:
            #debugging stuff (the print statements)
            #print(deriv,rightDeriv)
            #print("Deriv*",deriv*rightDeriv)
            #print("sign change:", x, deriv)
            if leftDeriv > 0:
                listMax.append(x)
            elif leftDeriv < 0:
                listMin.append(x)
        elif deriv == 0:
            if leftDeriv*rightDeriv < 0:
                print("sign change:", x)
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
    if len(listMax) > 0:
        print("Maxes at x =",listMax)
    else:
        print("No maximums")
    if len(listMin) > 0:
        print("Mins at x =",listMin)
    else:
        print("No minimums")
    absMaxFinder(listMax)
    absMinFinder(listMin)
    checkConcav(listPOI)
    #print(listDeriv)

def absMaxFinder(listMax): #finds the absolute minimum in a list of all minimums
    if len(listMax) > 0:
        if len(listMax) == 1:
            print('Absolute max at x =', listMax[0])
        else:
            largestX = listMax[0]
            for i in range(0,len(listMax)):
                if f(listMax[i]) > f(largestX):
                    largestX = listMax[i]
            print('Absolute max at x =', largestX)
    
def absMinFinder(listMin): #finds the absolute minimum in a list of all minimums
    if len(listMin) > 0:
        if len(listMin) == 1:
            print('Absolute min at x =', listMin[0])
        else:
            smallestX = listMin[0]
            for i in range(0,len(listMin)):
                if f(listMin[i]) < f(smallestX):
                    smallestX = listMin[i]
            print('Absolute min at x =', smallestX)

#intperets the function you enter
domainL = int(input("Enter the left bound of your domain: "))
domainH = int(input("Enter the right bound of your domain: "))
func = input("Input a function: ")

finder(100,domainL,domainH)


