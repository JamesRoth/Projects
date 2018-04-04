#James Roth
#4/4/18
#helicopterProjectMath.py

from math import *

def elev(xl,yl,E,A,Z):
    sina=degrees(sin(A))
    cosa=degrees(cos(A))
    tane=degrees(tan(E))
    return (((yl-sina*Z*tane)**2 + (xl-cosa*Z*tane))**2)**1/2/(Z-61)
    
print(elev(40.6,-106,77.6,23.1,408))
