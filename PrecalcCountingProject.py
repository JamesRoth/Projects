#James Roth/Charlie Adams
#Precalc Counting Project
#5/1/19

from random import *

#declaring variables:

N = 634     #number of parts
D = 7       #cost per defective part
G = 98      #% of good parts w/ both adjustments correct
K = 89      #% of good parts w/ one adjustments correct
W = 81      #% of good parts w/ no adjustment correct
M = 72      #cost of mechanic
S = 2       #cost per sample part

#figures out if a binary event happened with a certain probability
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
    for i in range(0,parts):
        if probability(chance) == 0:
            numDefective+=1
    return numDefective

#calculates the number of correct adjustments
def adjustments(mechanic):
    adjustProb = randint(1,100)
    if mechanic == 0:
        if adjustProb <= 80: #number of correct adjustments
            return 2
        elif adjustProb <= 95:
            return 1
        else:
            return 0
    else: #if the mechanic argument is anything but zero that means the mechanic is being called, so we return a value saying that both machines are correct
        return 2

#initializing the adjustments value, needs to happen after the adjustment function is defined
adj = 0
adj = adjustments(0)

#each different theoretical production strategy
def strat1Exp(adj, printer):
    cost1Exp = partsCost(1, adj) + M
    if printer == 1:
        print("Cost (strat 1): ", cost1Exp)
    return cost1Exp
    
def strat2Exp(adj,printer):
    cost2Exp = partsCost(0, adj)
    if printer == 1:
        print("Cost (strat 2): ", cost2Exp)
    return cost2Exp
    
def strat3Exp(adj,printer):
    #running the sample batch
    sampleAmount = []
    for i in range(1,5):
        sampleAmount.append(i)
    
    sampleCost = []
    totalCost = []
   
    for item in sampleAmount:
        sampleCost.append(S*item)
   
    #listing the cost of running all amounts of sample parts
    for i in range(0,(len(sampleAmount))):
        item = sampleAmount[i]
        if adj == 0:
            if noDefective(W/100, item) == 0:
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i] + partsCost(0, adj))
            else:
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i] + partsCost(1, adj) + M)
        elif adj == 1:
            if noDefective(K/100, item) == 0:
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i] + partsCost(0, adj))
            else:
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i] + partsCost(1, adj) + M)
        elif adj == 2:
            if noDefective(G/100, item) == 0:
                #finding the cost of the parts when none are defective
                totalCost.append(sampleCost[i] + partsCost(0, adj))
            else:
                #finding the cost of the parts when some are defective
                totalCost.append(sampleCost[i] + partsCost(1, adj) + M)
    
    if printer == 1:
        print("Cost (strat 3): ", totalCost)
    
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
            if probability(G/100) == 0:
                partsCostNum+=D
        elif adj == 1:
            if probability(K/100) == 0:
                partsCostNum+=D
        elif adj == 0:
            if probability(W/100) == 0:
                partsCostNum+=D
    return partsCostNum

#the theoretical cost of parts
def partsCostTheo(mechanic, noParts):
    partsCostNum = 0
    #if any sample parts are defective, we hire the mechanic 
    if mechanic == 1:
        partsCostNum+=(noParts*(100-G)/100)*D
    else:
        partsCostNum+= ((noParts*.8*(100-G)/100) + (noParts*.15*(100-K)/100) + (noParts*.05*(100-W)/100))*D
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
    for i in range(1,5):
        sampleAmount.append(i)
        
    #% of the time the master mechanic will be called for each amount of sample parts
    for i in range(0,len(sampleAmount)):
        samplePercentDefective.append(round(sampleAmount[i]*.8*(100-G) + sampleAmount[i]*.15*(100-K) + sampleAmount[i]*.05*(100-W)))
    #print("Percent defective: ", samplePercentDefective)
   
    #finding the total cost 
    for i in range(0,len(sampleAmount)):
        totalCost.append(("Samples",i+1))
        totalCost.append(round(samplePercentDefective[i]/100*M + partsCostTheo(1, (N*(samplePercentDefective[i]/100))) + partsCostTheo(0, (N*(1-(samplePercentDefective[i]/100)))),3) + (i+1)*S )
    print("Cost (strat 3) ", totalCost)

#a new experimental production run
def newRunExperimental(adj, printer):
    adj = adjustments(0)
    if printer == 1:
        print("Experimental:")
    strat1Exp(adj, printer)
    strat2Exp(adj, printer)
    strat3Exp(adj, printer)

#a new theoretical production run
def newRunTheoretical():
    print("Theoretical:")
    strat1Theo()
    strat2Theo()
    strat3Theo()

#a function that runs a lot of production runs and finds the average cost of each strat
def manyRuns(runs):
    newRunTheoretical()
    print("")
    print("Experimental - ",runs,"runs: ")
    costStrat1 = []
    costStrat2 = []
    costStrat3 = []
    for i in range(0, runs):
        adj = adjustments(0)
        costStrat1.append(strat1Exp(adj,0))
        costStrat2.append(strat2Exp(adj,0))
        costStrat3.append(strat3Exp(adj,0))
    print("Avg. cost strat 1: ", averageList(costStrat1))
    print("Avg. cost strat 2: ", averageList(costStrat2))
    print("Avg. cost strat 3: ", avgStrat3(costStrat3))

#gives the average cost for each amount of sample parts
def avgStrat3(list):
    avgCostStrat3 = []
    for i in range(0, len(list[0])):
        sum1 = 0
        avgCostStrat3.append(('Samples', i+1))
        for i2 in range(0,len(list[i])):
            sum1+=list[i2][i]
        avgCostStrat3.append(round(sum1/len(list[0])))
    return avgCostStrat3
    
    
#average value in a list
def averageList(list):
    return (sum(list)/len(list))

newRunExperimental(adj,0)
#manyRuns(500)


