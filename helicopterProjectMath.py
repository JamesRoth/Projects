#James Roth
#4/4/18
#helicopterProjectMath.py

from math import *

def elev(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    p1=(sina*Z*tane-yl)
    p2=(cosa*Z*tane-xl)
    ans=sqrt((p1**2+p2**2))/(Z-61)
    return str(degrees(atan(ans))) + " degrees"
    
print(elev(40.6,-106,77.6,23.1,408))

def beaconRange(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    p1=round((sina*Z*tane-yl), 4)
    p2=round((cosa*Z*tane-xl),4)
    d=sqrt((p1**2+p2**2))
    ans=sqrt((p1**2+p2**2))/(Z-61)
    angle=round(degrees(atan(ans)),4)
    #sin angle = d/range
    return str(d/sin(radians(angle))) + " meters"

print(beaconRange(40.6,-106,77.6,23.1,408))