def s(x1,x2,x3) :
    if (x1 or x2 or x3) :
        return True
    else : 
        return False

def n(x1,x2,x3) :
    if((x1 ^ x2) ^ x3) :
        return True
    else : 
        return False

def ns(x1,x2,x3) :
    if(not ((x1 ^ x2) and x3)) :
        return True
    else : 
        return False

def c(x1,x2,x3,y1,y2,y3) :
    if((x1 ^ x2) and (x2 ^ y2) and (x3 ^ y3)) :
        return True
    else : 
        return False

def isValid(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3) :
    # CANNOT BE: (A,B),(A,C),(A,E),(B,D),(C,E),(C,D),(D,F),(E,F)
    if((not(a1 and b1) or not(a2 and b2) or not(a3 and b3)) and \
    (not(a1 and c1) or not(a2 and c2) or not(a3 and c3)) and \
    (not(a1 and e1) or not(a2 and e2) or not(a3 and e3)) and \
    (not(b1 and d1) or not(b2 and d2) or not(b3 and d3)) and \
    (not(c1 and e1) or not(c2 and e2) or not(c3 and e3)) and \
    (not(c1 and d1) or not(c2 and d2) or not(c3 and d3)) and \
    (not(f1 and d1) or not(f2 and d2) or not(f3 and d3)) and \
    (not(f1 and e1) or not(f2 and e2) or not(f3 and e3))) :
        return True
    else : 
        return False