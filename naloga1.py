import math
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
        
def HX2(besedilo):
    n = 0
    i = []
    while(len(besedilo) > n):
        if(n + 1 >= len(besedilo)): break
        pr = besedilo.count(besedilo[n] + besedilo[n+1])/5
        if(pr == 0):
            continue
        a = pr * math.log2(pr)
        i.insert(n, a)
        n = n + 1
    
    return sum(i) * (-1) - HX1(besedilo)

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
        H = HX2(besede)
    elif(p == 2):
        s

    print(H)
    return 1



naloga1("AbB,a.bC",1)