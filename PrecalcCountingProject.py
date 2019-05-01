#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *

N = 634
D = 7
G = 98
K = 89
W = 81
M = 72
S = 2

adjustProb = randint(0,100)

def noDefective(chance,parts):
    numDefective = 0
    for i in range(1,parts+1):
        if 

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
def strat1Theo():
    cost1Theo = M
    adjustments(1)
    
    
def strat2Theo():
    cost2Theo = 0
    adjustments(0)
    
    
def strat3Theo():
    cost3Theo = 0
    adjustments(0)
    
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)
    sampleCost = []
    for item in sampleAmount:
        sampleCost.append(item*S)
    

#strat3Theo()

def strat1Exp():
    adjustments(1)
    
def strat2Exp():
    adjustments(0)
    
def strat3Exp():
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)

