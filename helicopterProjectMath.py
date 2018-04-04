#James Roth
#4/4/18
#helicopterProjectMath.py

from math import *

def elev(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    sina=degrees(sina)
    cosa=degrees(cosa)
    tane=degrees(tane)
    ansrad=((((yl-sina*Z*tane)**2 + (xl-cosa*Z*tane))**2)**1/2)/(Z-61)
    print(ansrad)
    return atan(radians(ansrad)) #should work but doesnt - why?
    
print(elev(40.6,-106,77.6,23.1,408))
