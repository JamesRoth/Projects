#James Roth
#11/21/19
#LRAM, MRAM, RRAM - finding the area under a curve with different estimations

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

def f(xVal):
    x=xVal
    return(eval(func))

func = input("Input a function: ")
intervalLow = int(input("Enter the lower bound of your interval: "))
intervalHigh = int(input("Enter the higher bound of your interval: "))
interval = int(input("Enter the interval value: "))
lRam = 0
rRam = 0
mRam = 0

base = (intervalHigh-intervalLow)/interval

for i in range(0,interval):
    #LRAM
    lRam = lRam + f(intervalLow+i/(interval/(intervalHigh-intervalLow)))*base
    
for i in range(1,interval+1):
    #RRAM
    rRam = rRam + f(intervalLow+i/(interval/(intervalHigh-intervalLow)))*base

for i in range(0,interval):
    #MRAM
    mRam = mRam + f((base/2+intervalLow+i/(interval/(intervalHigh-intervalLow))))*base
    
trap = (lRam+rRam)/2
print("LRAM: ", lRam)
print("MRAM: ", mRam)
print("RRAM: ", rRam)
print("TRAP: ", trap)
print("Simpson's: ", (mRam*2+trap)/3)

    
    

