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
    return "ELEV = " + str(round(degrees(atan(ans)),4)) + " degrees"

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
    return "AZIM = " + str(round(d/sin(radians(angle)),4)) + " meters"

print(elev(40.6,-106,77.6,23.1,408))
print(elev(40.6,-106,77.9,146.7,408))
print(elev(40.6,-106,77.5,201.8,408))
print(elev(40.6,-106,78.0,330.0,408))
print(beaconRange(40.6,-106,77.6,23.1,408))
print(beaconRange(40.6,-106,77.9,146.7,408))
print(beaconRange(40.6,-106,77.5,201.8,408))
print(beaconRange(40.6,-106,78.0,330.0,408))