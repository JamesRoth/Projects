#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *

#declaring variables:

N = 634     #number of parts
N = 6       #this N for testing purposes only
D = 7       #cost per defective part
G = 98      #% of good parts w/ both adjusments correct
K = 89      #% of good parts w/ one adjusments correct
W = 81      #% of good parts w/ no adjusment correct
M = 72      #cost of mechanic
S = 2       #cost per test part?

adj = 0

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

#calculates the number of correct adjustments
def adjustments(mechanic):
    if mechanic == 0:
        if adjustProb <= 80: #number of correct adjustments
            global adj
            adj = 2
        elif adjustProb <= 95:
            global adj 
            adj = 1
        else:
            global adj 
            adj = 0
    else: #if the mechanic argument is anything but zero that means the mechanic is being called, so we return a value saying that both machines are correct
        global adj 
        adj = 2

#each different theoretical production strategy
def strat1Theo():
    cost1Theo = M + partsCost(1)
    print("Cost (strat 1): ", cost1Theo)
    
def strat2Theo():
    cost2Theo = partsCost(0)
    print("Cost (strat 2): ", cost2Theo)
    
def strat3Theo():
    cost3Theo = 0
    
    #running the sample batch
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)
    
    sampleCost = []
    totalCost = []
   
    #listing the cost of running all amounts of sample parts
    mechanic = 0
    for i in range(0,(len(sampleAmount))):
        item = sampleAmount[i]
        if adj == 0:
            if noDefective(W/100, item) == 0:
                sampleCost.append(S*item)
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i]+partsCost(0))
            else:
                sampleCost.append(S*item+M)
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i]+partsCost(1))
        elif adj == 1:
            if noDefective(K/100, item) == 0:
                sampleCost.append(S*item)
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i]+partsCost(0))
            else:
                sampleCost.append(S*item+M)
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i]+partsCost(1))
        elif adj == 2:
            if noDefective(G/100, item) == 0:
                sampleCost.append(S*item)
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i]+partsCost(0))
            else:
                sampleCost.append(S*item+M)
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i]+partsCost(1))
    
    #debugging purposes only:
    print("(Strat 3): Sample amount: ", sampleAmount)
    print("(Strat 3): Total cost: ", totalCost)

#gives us the cost of parts 
def partsCost(mechanic):
    #if any sample parts are defective, we hire the mechanic (for strategy 3 this cost, however, is accounted for in the sampleCost list, so we don't need to add it
    if mechanic == 1:
        adjustments(mechanic)
    
    #costs from defective parts - "creates" all the parts and accounts for costs for each defective one
    partsCostNum = 0
    for i in range(0,N):
        if adj == 0:
            if probability(W/100) == 0:
                partsCostNum+=D
        elif adj == 1:
            if probability(K/100) == 0:
                partsCostNum+=D
        elif adj == 2:
            if probability(G/100) == 0:
                partsCostNum+=D
    return partsCostNum

#each different experimental production strategy
def strat1Exp():
    print("")
    
def strat2Exp():
    print("")
    
def strat3Exp():
    sampleAmount = []
    for i in range(1, N+1):
        sampleAmount.append(i)


def newRunTheoretical():
    adjustments(0)
    strat1Theo()
    strat2Theo()
    strat3Theo()

def newRunExperimental():
    adjustments(0)

newRunTheoretical()


