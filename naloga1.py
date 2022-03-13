from collections import Counter
import math

#-------------------------------------------------------------------------------------------------------------------------#

# All possible letter from the english alphabet.

letters = ['a','b','c','d','e','f','g','h','i', 'j', 'k','l','m','n','o' ,'p','q','r','s','t','u','v','w','y','x','z']

#-------------------------------------------------------------------------------------------------------------------------#

# A function that returns True if the character is from the english alphabet.

def fun(variable):
    if (variable in letters):
        return True
    else:
        return False

#-------------------------------------------------------------------------------------------------------------------------#

# A function that calculates the entropy of a single letter.

def HX1(besedilo):
    l = 0
    i = []
    for s in letters:
        pr = besedilo.count(s)/len(besedilo)
        if(pr == 0):
            continue
        a = pr * math.log2(pr)
        i.insert(l, a)
        l = l + 1

    return sum(i) * (-1) 

#-------------------------------------------------------------------------------------------------------------------------#

# A function that calculates the entropy of two letters.

def HX2(besedilo, bool):
    lit = []
    cou = Counter(zip(besedilo, besedilo[1:]))

    for l in cou.values():
        if(l in lit): continue
        pr = l/(len(besedilo)-1)
        if(pr == 0): continue 
        a = pr * math.log2(pr)
        lit.append(a)
    if(bool == 1): return sum(lit) * (-1)
    return sum(lit) * (-1) - HX1(besedilo)

#-------------------------------------------------------------------------------------------------------------------------#

# A function that calculates the entropy of three letters.

def HX3(besedilo):

    lit = []
    cou = Counter(zip(besedilo, besedilo[1:], besedilo[2:]))

    for l in cou.values():
        if(l in lit): continue
        pr = l/(len(besedilo)-2)
        if(pr == 0): continue 
        a = pr * math.log2(pr)
        lit.append(a)

    return sum(lit) * (-1) - HX2(besedilo, 1)

#-------------------------------------------------------------------------------------------------------------------------#

# Function that starts the program. It calls the functions based on given parameters.

def naloga1(besedilo, p):

    filtered = filter(fun, list(str.lower(besedilo)))

    besede = "".join(filtered)
    
    if(p == 0):
        H = HX1(besede)
    elif(p == 1):
        H = HX2(besede, 0)
    elif(p == 2):
        H = HX3(besede)

    return round(H, 4)
