#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *

N = 634     #number of parts
D = 7       #
G = 98      #% of good parts w/ both adjusments correct
K = 89      #% of good parts w/ one adjusments correct
W = 81      #% of good parts w/ no adjusment correct
M = 72      #cost of mechanic
S = 2       #cost per test part?

adjustProb = randint(1,100)

def probability(chance):
    num = randint(1,100)
    if num <= (chance*100):
        return 1
    else: 
        return 0

def noDefective(chance,parts):
    numDefective = 0
    for i in range(1,parts+1):
        if probability(chance) == 0:
            numDefectice+=1

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
    
    #running the sample batch
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)
    sampleCost = []
    for item in sampleAmount:
        sampleCost.append(item*S)
    #checking the cost of running different amounts of samples
    for item in sampleAmount:
        if adj == 0:
            if noDefective(0.8, item) == 0:
                
            else:
                cost3Theo+= M
    

#strat3Theo()

def strat1Exp():
    adjustments(1)
    
def strat2Exp():
    adjustments(0)
    
def strat3Exp():
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)

