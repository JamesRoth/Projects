#James Roth
#11/21/19
#LRAM, MRAM, RRAM - finding the area under a curve with different estimations

from math import sin, cos, tan, acos, asin, atan
from math import exp, e, pi
from math import log, log10, sqrt, log2

def f(xVal):
    x=xVal
    return(eval(func))

func = input("Input a function: ”)
intervalLow = int(input("Enter the lower bound of your interval: "))
intervalHigh = int(input("Enter the higher bound of your interval: "))
interval = int(input("Enter the interval value: "))
lRam = 0
rRam = 0
mRam = 0

base = (intervalHigh-intervalLow)/interval
for i in range(0,interval):
    #LRAM
    lRam += f(i/interval)*base
    
