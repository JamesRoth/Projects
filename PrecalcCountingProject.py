#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *

N = 634
D = 7
G = 98
K = 89
W = 81
N = 72
S = 2

adjustProb = randint(0,100)

def newRunTheoretical():
    adjustments(0)

def newRunExperimental():
    adjustments(0)

def adjustments(mechanic):
    if mechanic == 0:
        if adjustProb <= 80: #number of correct adjustments
            adj = 2
        elif adjustProb <= 95:
            adj = 1
        else:
            adj = 0
    else:
        adj = 2


#each different production strategy
def strat1():
    adjustments(1)
    
def strat2():
    adjustments(0)
    
def strat3():
    sampleAmount = range(N)
    print(sampleAmount)
    
strat3()

