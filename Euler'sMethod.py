#James Roth
#12/19/19
#Euler'sMethod.py - a program to solve euler's method

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

#evaluates functions
def f(xVal,yVal):
    x=xVal
    y=yVal
    return(eval(func))

#standard run of input statements
func = input("Enter a function (g(x), or dy/dx): ")
startX = float(input("Enter the starting x-value: "))
startY = float(input("Enter the starting y-value: "))
endX = float(input("Enter the ending x-value: "))
n = int(input("Enter the n-value you want: "))

#variables:
deltaX = (endX - startX)/n
currentX = startX
currentY = startY
slope = 0

#main loop:
for i in range(0,n):
    slope = f(currentX,currentY)
    currentX+=deltaX
    currentY+=(slope*deltaX)

print(round(currentX,8), round(currentY,8))

