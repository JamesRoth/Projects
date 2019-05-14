#James Roth
#5/14/19
#DartmouthCoderDojo.py - Dartmouth students teaching elements of python

def sumList(A):
    if len(A) == 0:
        return 0
    else:
        return A[0] + sumList(A[1:])


sumList([1,2,3,4,5,6,7,8])