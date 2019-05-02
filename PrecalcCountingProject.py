#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *

#declaring variables:

N = 634     #number of parts
N = 6       #this N for testing purposes only
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
        #event happened
        return 1
    else: 
        #event didn't happen
        return 0

#tells us if any parts are defective so we know to call the mechanic
def noDefective(chance,parts):
    numDefective = 0
    for i in range(1,parts+1):
        if probability(chance) == 0:
            numDefective+=1
    return numDefective

def newRunTheoretical():
    global adj
    adj = adjustments(0)

def newRunExperimental():
    global adj
    adj = adjustments(0)

#calculates the number of correct adjustments
def adjustments(mechanic):
    if mechanic == 0:
        if adjustProb <= 80: #number of correct adjustments
            return 2
        elif adjustProb <= 95:
            return 1
        else:
            return 0
    else: #if the mechanic argument is anything but zero that means the mechanic is being called, so we return a value saying that both machines are correct
        return 2

#each different production strategy
def strat1Theo():
    cost1Theo = M
    
    
def strat2Theo():
    cost2Theo = 0
    
    
def strat3Theo():
    cost3Theo = 0
    adj = adjustments(0)
    
    #running the sample batch
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)
    
    sampleCost = []
   
    #listing the cost of running all amounts of sample parts
    mechanic = 0
    for item in sampleAmount:
        if adj == 0:
            if noDefective(W/100, item) == 0:
                sampleCost.append(S*item)
                partsAndSampleCost(0)
            else:
                sampleCost.append(S*item+M)
                partsAndSampleCost(1)
        elif adj == 1:
            if noDefective(K/100, item) == 0:
                sampleCost.append(S*item)
                partsAndSampleCost(0)
            else:
                sampleCost.append(S*item+M)
                mechanic = 1
                partsAndSampleCost(1)
        elif adj == 2:
            if noDefective(G/100, item) == 0:
                sampleCost.append(S*item)
                partsAndSampleCost(0)
            else:
                sampleCost.append(S*item+M)
                partsAndSampleCost(1)
    
    print(sampleAmount)
    print(sampleCost)
    
    #adding up total cost:
    finalCost = []
    for item in sampleCost:
        finalCost.append

#gives us the cost of parts and their accompanying sample
def partsAndSampleCost(mechanic):
    #if any sample parts are defective, we hire the mechanic
    if mechanic == 1:
        adjustments(mechanic)
    
    #costs from defective parts
    partsCost = 0
    for i in range(0,N):
        if adj == 0:
            
        elif adj == 1:
            
        elif adj == 2:
            if probability(G/100) == 0:
                partsCost = 

strat3Theo()

def strat1Exp():
    print("")
    
def strat2Exp():
    print("")
    
def strat3Exp():
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)

