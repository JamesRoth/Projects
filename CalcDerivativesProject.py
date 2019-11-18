#James and Alex Roth
#11/12/19
#Calc derivative project

#all of this is the function interperter, our code starts at line 134
import math
def int_checker(string):
    ans=True
    for x in string:
        if not(x in set(['1','2','3','4','5','6','7','8','9','0','.',',','-'])):
            ans=False
    return ans
def find_loci(string, sym):
    paren=0
    for x in range(len(string)):
        if string[x]==sym and paren<1:
            return x
        elif string[x]=='(':
            paren+=1
        elif string[x]==')':
            paren-=1
    return False
def all_in_paren(string):
    if string[0]=='(' and string[-1]==')' and not('(' in set(string[1:-1]) or '(' in set(string[1:-1])):
        return True
    else:
        return False
#everything above sets up functions that will be necessary for the one below

def individual_perform(equ):
    if all_in_paren(equ):
        return individual_perform(equ[1:-1])
    elif int_checker(equ)==True:
        def ans(x):
            return eval(equ)
    elif find_loci(equ, '+')!=False:
        sym_loci=find_loci(equ,'+')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)+individual_perform(post)(x)
    elif find_loci(equ, '-')!=False:
        sym_loci=find_loci(equ,'-')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)-individual_perform(post)(x)
    elif find_loci(equ, '*')!=False:
        sym_loci=find_loci(equ,'*')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)*individual_perform(post)(x)
    elif find_loci(equ, '/')!=False:
        sym_loci=find_loci(equ,'/')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)/individual_perform(post)(x)
    elif find_loci(equ,'^')!=False:
        sym_loci=find_loci(equ, '^')
        pre= equ[:sym_loci]
        post= equ[sym_loci+1:]
        def ans(x):
            return individual_perform(pre)(x)**individual_perform(post)(x)
    elif equ[:3]=='sin':
        contents=equ[3:]
        def ans(x):
            return math.sin(individual_perform(contents)(x))
    elif equ[:3]=='cos':
        contents=equ[3:]
        def ans(x):
            return math.cos(individual_perform(contents)(x))
    elif equ[:3]=='tan':
        contents=equ[3:]
        def ans(x):
            return math.tan(individual_perform(contents)(x))
    elif equ[:3]=='csc':
        contents=equ[3:]
        def ans(x):
            return 1/math.sin(individual_perform(contents)(x))
    elif equ[:3]=='sec':
        contents=equ[3:]
        def ans(x):
            return 1/math.cos(individual_perform(contents)(x))
    elif equ[:3]=='cot':
        contents=equ[3:]
        def ans(x):
            return 1/math.tan(individual_perform(contents)(x))
    elif equ[:3]=='log':
        end=find_loci(equ,'_')
        base=equ[3:end]
        def ans(x):
            return math.log(x)/math.log(base)
    elif equ=='e':
        def ans(x):
            return math.e
    elif equ=='pi':
        def ans(x):
            return math.pi
    elif equ[:3]=='asin':
        contents=equ[3:]
        def ans(x):
            return math.asin(individual_perform(contents)(x))
    elif equ[:3]=='acos':
        contents=equ[3:]
        def ans(x):
            return math.acos(individual_perform(contents)(x))
    elif equ[:3]=='atan':
        contents=equ[3:]
        def ans(x):
            return math.atan(individual_perform(contents)(x))
    elif equ[:3]=='acsc':
        contents=equ[3:]
        def ans(x):
            return 1/math.asin(individual_perform(contents)(x))
    elif equ[:3]=='asec':
        contents=equ[3:]
        def ans(x):
            return 1/math.acos(individual_perform(contents)(x))
    elif equ[:3]=='acot':
        contents=equ[3:]
        def ans(x):
            return 1/math.atan(individual_perform(contents)(x))
    else:
        def ans(x):
            return x
    return ans
    
#function_1=individual_perform(func_1)

#delcaring varialbes
tolerance = 0.001
listMax = []
listMin = []
listDeriv = []
listPOI = []

#functions
def f(x): #the function we are currently finding all the info for
    #func_1='cos(x*pi)+x^3'
    #return(function_1(x))
    return x**2

def numDeriv(x,h): #finds the numerical derivative at a point
    ans = (f(x+h) - f(x-h))/(2*h)
    #return round(ans,3) 
    return ans
    
def numDerivLeft(x,h): #does derivative at the left endpoint
    ans = (f(x+h) - f(x))/(h)
    #return round(ans,3) 
    return ans

def numDerivRight(x,h): #does derivative at the right endpoint
    ans = (f(x-h) - f(x))/(-h) # I added the - to the h and hopefully it'll fix the problem, but we need to find WHY it fixes the problem
    #return round(ans,3) 
    return ans

def numSecDeriv(x,h): #finds the second derivative at x
    leftDeriv = numDeriv(x-h, h)
    rightDeriv = numDeriv(x+h,h)
    #return round((leftDeriv - rightDeriv)/(2*h),3) 
    return (leftDeriv - rightDeriv)/(2*h)

def checkIncDec(listMax,listMin): #finds where the function is increasing and decreasing
    listExtreme = listMax + listMin
    listExtreme.sort()
    for i in range (0, len(listExtreme)-1):
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) < 0:
                print("Decreasing from",listExtreme[i],"to ",listExtreme[i + 1])
            if numDeriv((listExtreme[i] + listExtreme[i + 1])/2, tolerance) > 0:
                print("Increasing from",listExtreme[i],"to ",listExtreme[i + 1])

def checkConcav(listPOI): #finds where the function is concave up/concave down
    listPOI.sort()
    for i in range (0, len(listPOI)-1):
        if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) > 0:
            print("Concave down from",listPOI[i],"to ",listPOI[i + 1])
        if numSecDeriv((listPOI[i] + listPOI[i + 1])/2, tolerance) < 0:
            print("Concave up from",listPOI[i],"to ",listPOI[i + 1])

def finder(stepDeriv,domainLow,domainHigh): #finds all of the information we want to know, the "master function"
    listMin = []
    listMax = []
    listPOI = [] #has endpoints as well as POIs
    listPOI.append(domainLow)
    x = round(domainLow) #left endpoint case
    val = numDerivLeft(x,tolerance) #just using this variable so I only calculate this number once
    if val > 0:
        listMin.append(domainLow)
    elif val < 0:
        listMax.append(domainLow)
    for i in range (1, stepDeriv*abs(domainLow-domainHigh)-1):
        x = (domainLow+i/stepDeriv)
        leftDeriv = numDeriv(x-(1/stepDeriv), tolerance)
        rightDeriv = numDeriv(x+(1/stepDeriv),tolerance)
        deriv = numDeriv(x,tolerance)
        listDeriv.append(numDeriv(x,tolerance))
        #first derivative stuff
        if deriv*numDeriv(x+(1/stepDeriv),tolerance) < 0 and deriv != 0: #not recognizing both sides of the zero
            print("sign change", x)
            if leftDeriv > 0:
                listMax.append(x)
            elif leftDeriv < 0:
                listMin.append(x)
        elif deriv == 0:
            if leftDeriv*rightDeriv < 0:
                print("sign change", x)
            if leftDeriv > 0:
                listMax.append(x)
            elif leftDeriv < 0:
                listMin.append(x)
        #second derivative stuff
        if numSecDeriv(x, tolerance)*numSecDeriv(x+(1/stepDeriv),tolerance) < 0:
            listPOI.append(x)
            print("POI at ",x)
    x = round(domainHigh) #right endpoint case
    val = numDerivRight(x,tolerance) #just using this variable so I only calculate this number once
    if val > 0:
        listMax.append(domainHigh)
    elif val < 0:
        listMin.append(domainHigh)
    listPOI.append(domainHigh)
    checkIncDec(listMax,listMin)
    if len(listMax) > 0:
        print("Maxes at x =",listMax)
    else:
        print("No maximums")
    if len(listMin) > 0:
        print("Mins at x =",listMin)
    else:
        print("No minimums")
    absMaxFinder(listMax)
    absMinFinder(listMin)
    checkConcav(listPOI)
    #print(listDeriv)

def absMaxFinder(listMax): #finds the absolute minimum in a list of all minimums
    if len(listMax) > 0:
        if len(listMax) == 1:
            print('Absolute max at x =', listMax[0])
        else:
            largestX = listMax[0]
            for i in range(0,len(listMax)):
                if f(listMax[i]) > f(largestX):
                    largestX = listMax[i]
            print('Absolute max at x =', largestX)
    
def absMinFinder(listMin): #finds the absolute minimum in a list of all minimums
    if len(listMin) > 0:
        if len(listMin) == 1:
            print('Absolute min at x =', listMin[0])
        else:
            smallestX = listMin[0]
            for i in range(0,len(listMin)):
                if f(listMin[i]) < f(smallestX):
                    smallestX = listMin[i]
            print('Absolute min at x =', smallestX)

#intperets the function you enter
func_1 = input("Enter your function, but please remember proper syntax: When typing the function, don’t include spaces. You also have to stick to certain syntax. ^ is used to bring a number to a power, while * is for multiplication exclusively. I can’t promise it will work if you input commas. Division is done by /, and it includes all trig functions and their inverses (with the inverse notation being asin instead of sin, acsc instead of csc, etc.) When inputting a logarithm, you first type log, then the base, then _, then the number whose log you want to find. Ln isn’t a working command, but the program can recognize both e and pi (typed as seen here).It follows general order of operations (although it recognizes only parentheses, not brackets) but also prioritizes the positive direction of the negative (addition before subtraction, multiplication before division). ")
function_1=individual_perform(func_1)

finder(100,-2,2)


