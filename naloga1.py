import math
from pickle import FALSE, TRUE
from sympy import S

letters = ['a','b','c','d','e','f','g','h','i', 'j', 'k','l','m','n','o' ,'p','q','r','s','t','u','v','w','y','x','z']

def fun(variable):
    if (variable in letters):
        return True
    else:
        return False

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
        
def HX2(besedilo, bool):
    n = 0
    i = []
    lit = []
    while(len(besedilo) > n):
        if(n + 1 >= len(besedilo)): break
        if((besedilo[n]+besedilo[n+1]) in lit): 
            n = n + 1
            continue
        lit.append(besedilo[n]+besedilo[n+1])
        pr = besedilo.count(besedilo[n] + besedilo[n+1])/(len(besedilo)-1)
        if(pr == 0):
            continue
        a = pr * math.log2(pr)
        i.insert(n, a)
        n = n + 1
    
    return sum(i) * (-1) - HX1(besedilo)
    

def HX3(besedilo):
    n = 0
    i = []
    lit = []
    while(len(besedilo) > n):
        if(n + 2 >= len(besedilo)): break
        if((besedilo[n]+besedilo[n+1]+besedilo[n+2]) in lit): 
            n = n + 1
            continue
        lit.append(besedilo[n]+besedilo[n+1]+besedilo[n+2])
        pr = besedilo.count(besedilo[n] + besedilo[n+1] + besedilo[n+2])/(len(besedilo)-2)
        if(pr == 0):
            continue
        a = pr * math.log2(pr)
        i.insert(n, a)
        n = n + 1
    
    return sum(i) * (-1) - HX2(besedilo, 0)

def naloga1(besedilo, p):
    
    """ Izracun povprecne nedolocenosti na znak 

    Parameters
    ----------
    besedilo : str
        Vhodni niz
    p : int
        Stevilo poznanih predhodnih znakov: 0, 1 ali 2.
        p = 0: H(X1)
            racunamo povprecno informacijo na znak abecede 
            brez poznanih predhodnih znakov
        p = 1: H(X2|X1)
            racunamo povprecno informacijo na znak abecede 
            pri enem poznanem predhodnemu znaku 
        p = 2: H(X3|X1,X2)

    Returns
    -------
    H : float 
        Povprecna informacija na znak abecede z upostevanjem 
        stevila poznanih predhodnih znakov 'p'
    """

    filtered = filter(fun, list(str.lower(besedilo)))

    besede = "".join(filtered)
    
    

    if(p == 0):
        H = HX1(besede)
    elif(p == 1):
        H = HX2(besede, 1)
    elif(p == 2):
        H = HX3(besede)

    return round(H, 4)
