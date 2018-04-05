#James Roth
#4/4/18
#helicopterProjectMath.py

from math import *

def elev(xl,yl,E,A,Z):
    sina=sin(radians(A))
    cosa=cos(radians(A))
    tane=tan(radians(E))
    print(sina,cosa,tane,"SPACE")
    p1=round((sina*Z*tane-yl), 4)
    p2=round((cosa*Z*tane-xl),4)
    print(p1,p2,"SPACE")
    print(sqrt((p1**2+p2**2)),"SPACE")
    ans=sqrt((p1**2+p2**2))/(Z-61)
    print(ans)
    return degrees(atan(ans)) #should work but doesnt - why?
    
print(elev(40.6,-106,77.6,23.1,408))