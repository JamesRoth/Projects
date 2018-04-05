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
    return "ELEV = " + str(round(degrees(atan(ans)),2)) + " degrees"

def azim(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    p1=(sina*Z*tane-yl)
    p2=(cosa*Z*tane-xl)
    ans=sqrt((p1**2+p2**2))
    if A>270:
        return "AZIM = " + str(round(360-degrees(acos((p2)/ans)),2)) + " degrees"
    elif A>180:
        return "AZIM = " + str(round(180 + (180-degrees(acos((p2)/ans))),2)) + " degrees"
    else:
        return "AZIM = " + str(round(degrees(acos((p2)/ans)),2)) + " degrees"

def beaconRange(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    p1=(sina*Z*tane-yl)
    p2=(cosa*Z*tane-xl)
    d=sqrt((p1**2+p2**2))
    ans=sqrt((p1**2+p2**2))/(Z-61)
    angle=degrees(atan(ans))
    #sin angle = d/range
    return "RANGE = " + str(round(d/sin(radians(angle)),2)) + " meters"

print(elev(40.6,-106,77.6,23.1,408))
print(elev(40.6,-106,77.9,146.7,408))
print(elev(40.6,-106,77.5,201.8,408))
print(elev(40.6,-106,78.0,330.0,408))
print(azim(40.6,-106,77.6,23.1,408))
print(azim(40.6,-106,77.9,146.7,408))
print(azim(40.6,-106,77.5,201.8,408))
print(azim(40.6,-106,78.0,330.0,408))
print(beaconRange(40.6,-106,77.6,23.1,408))
print(beaconRange(40.6,-106,77.9,146.7,408))
print(beaconRange(40.6,-106,77.5,201.8,408))
print(beaconRange(40.6,-106,78.0,330.0,408))