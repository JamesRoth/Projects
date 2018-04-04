#James Roth
#4/4/18
#helicopterProjectMath.py



def elev(xl,yl,E,A,Z):
    return((yl-sin(A)*Z*tan(E))**2 + (xl-cos(A)*Z*tan(E))**2)**1/2)/z-61
    
print(elev(40.6,-106,77.6,23.1,408))
