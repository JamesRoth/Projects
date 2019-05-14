#James Roth
#5/14/19
#DartmouthCoderDojo.py - Dartmouth students teaching elements of python

def sumList(A):
    if len(A) == 0:
        return 0
    else:
        return A[0] + sumList(A[1:])

print(sumList([1,2,3,4,5,6,7,8]))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(9))
