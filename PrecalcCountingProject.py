#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *
from math import floor

#declaring variables:

N = 634     #number of parts
D = 7       #cost per defective part
G = 98      #% of good parts w/ both adjusments correct
K = 89      #% of good parts w/ one adjusments correct
W = 81      #% of good parts w/ no adjusment correct
M = 72      #cost of mechanic
S = 2       #cost per sample part

adj = 0

adjustProb = randint(1,100)

#generates new numbers for the inital values for the project
def generateNewNums():
    N = randint(300,1000)
    D = randint(3,9)
    G = randint(96,99)
    K = randint(88,92)
    W = randint(78,84)
    M = randint(50,100)
    S = randint(2,6)

#figures out if an event happened with a certain probability
def probability(chance):
    num = randint(1,100)
    if num <= (chance*100):
        #event happened
        return 1
    else: 
        #event didn't happen
        return 0

#returns the number of defective parts for a select number and chance
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
            return 2
        elif adjustProb <= 95:
            return 1
        else:
            return 0
    else: #if the mechanic argument is anything but zero that means the mechanic is being called, so we return a value saying that both machines are correct
        return 2

#each different theoretical production strategy
def strat1Exp(adj):
    cost1Exp = M + partsCost(1, adj)
    print("Cost (strat 1): ", cost1Exp)
    return cost1Exp
    
def strat2Exp(adj):
    cost2Exp = partsCost(0, adj)
    print("Cost (strat 2): ", cost2Exp)
    return cost2Exp
    
def strat3Exp(adj):
    
    #running the sample batch
    sampleAmount = []
    for i in range(1,6):
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
                totalCost.append(sampleCost[i]+partsCost(0, adj))
            else:
                sampleCost.append(S*item+M)
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i]+partsCost(1, adj))
        elif adj == 1:
            if noDefective(K/100, item) == 0:
                sampleCost.append(S*item)
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i]+partsCost(0, adj))
            else:
                sampleCost.append(S*item+M)
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i]+partsCost(1, adj))
        elif adj == 2:
            if noDefective(G/100, item) == 0:
                sampleCost.append(S*item)
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i]+partsCost(0, adj))
            else:
                sampleCost.append(S*item+M)
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i]+partsCost(1, adj))
    
    #debugging purposes only:
    print("(Strat 3): Total cost: ", totalCost)
    return totalCost

#gives us the cost of parts - for experimental
def partsCost(mechanic, adj):
    #if any sample parts are defective, we hire the mechanic 
    if mechanic == 1:
        adj = 2
    #costs from defective parts - "creates" all the parts and accounts for costs for each defective one
    partsCostNum = 0
    for i in range(0,N):
        if adj == 2:
            if probability(W/100) == 0:
                partsCostNum+=D
        elif adj == 1:
            if probability(K/100) == 0:
                partsCostNum+=D
        elif adj == 0:
            if probability(G/100) == 0:
                partsCostNum+=D
    return partsCostNum

#the theoretical cost of parts
def partsCostTheo(mechanic, noParts):
    partsCostNum = 0
    
    #if any sample parts are defective, we hire the mechanic 
    if mechanic == 1:
        partsCostNum+=(noParts*(100-G)/100)*D
    else:
        partsCostNum+=(noParts*.8*(100-G)/100)*D+(noParts*.15*(100-K)/100)*D+(noParts*.05*(100-W)/100)*D
    return partsCostNum

#each different theroetical production strategy
def strat1Theo():
    cost1Theo = partsCostTheo(1,N) + M
    print("Cost (strat 1): ",cost1Theo)
    
def strat2Theo():
    cost2Theo = partsCostTheo(0,N)
    print("Cost (strat 2): ",cost2Theo)
    
def strat3Theo(): 
    sampleAmount = []
    samplePercentDefective = []
    totalCost = []
    
    #different numbers of sample parts
    for i in range(1,6):
        sampleAmount.append(i)
        
    #% of the time the master mechanic will be called for each amount of sample parts
    for i in range(0,len(sampleAmount)):
        samplePercentDefective.append(round(sampleAmount[i]*.8*(100-G) + sampleAmount[i]*.15*(100-K) + sampleAmount[i]*.05*(100-W)))
    #print("Percent defective: ", samplePercentDefective)
   
    #finding the total cost - 
    for i in range(0,len(sampleAmount)):
        totalCost.append(round(samplePercentDefective[i]/100*M + partsCostTheo(1, (N*samplePercentDefective[i]/100)) + partsCostTheo(0, (N*(1-(samplePercentDefective[i]/100)))),3) + (i+1)*S )
    print("Total cost (strat 3) ", totalCost)

#a new experimental production run
def newRunExperimental(adj):
    adj = adjustments(0)
    print("Experimental:")
    strat1Exp(adj)
    strat2Exp(adj)
    strat3Exp(adj)

#a new theoretical production run
def newRunTheoretical():
    print("Theoretical:")
    strat1Theo()
    strat2Theo()
    strat3Theo()

#a function that runs a lot of production runs and finds the average cost of each strat
def manyRuns(runs):
    costStrat1 = []
    costStrat2 = []
    costStrat3 = []
    for i in range(0, runs):
        adj = adjustments(0)
        costStrat1.append(strat1Exp(adj))
        costStrat2.append(strat2Exp(adj))
        costStrat3.append(strat3Exp(adj))
    print("Avg. cost strat 1: ", averageList(costStrat1))
    print("Avg. cost strat 2: ", averageList(costStrat2))
    print("Avg. cost strat 3: ", avgStrat3(costStrat3))

def avgStrat3(list):
    sum = 0
    avgCostStrat3 = []
    for i in range(0, len(list[0])):
        avgCostStrat3.append(('Samples', i+1))
        for i2 in range(0,len(list[i])):
            sum+=list[i2][i]
        avgCostStrat3.append(round(sum/len(list[0])))
    return avgCostStrat3
    
    
#average value in a list
def averageList(list):
    return (sum(list)/len(list))

newRunExperimental(adj)
#newRunTheoretical()
#manyRuns(10)

