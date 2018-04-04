#James Roth
#4/4/18
#helicopterProjectMath.py

from math import *

def elev(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    ansrad=((((yl-sina*Z*tane)**2 + (xl-cosa*Z*tane))**2)**1/2)/(Z-61)
    print(ansrad)
    return atan(ansrad) #should work but doesnt - why?
    
print(elev(40.6,-106,77.6,23.1,408))
