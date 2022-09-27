def s(x1,x2,x3) :
    if (x1 or x2 or x3) :
        return True
    else : 
        return False

def n(x1,x2,x3) :
    if(((x1 ^ x2 ^ x3) and not(x1 and x2 and x3)) or (not(x1 ^ x2 ^ x3) and (not x1 and not x2 and not x3))):
        return True
    else : 
        return False

def ns(x1,x2,x3) :
    if((x1 ^ x2 ^ x3) and not(x1 and x2 and x3)) :
        return True
    else : 
        return False

def c(x1,x2,x3,y1,y2,y3) :
    if ((x1 and y1) or (x2 and y2) or (x3 and y3)) : 
        return False
    else :
        return True


def isValid(a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3) :
    if(
    ((not a1 and not b1) ^ (not a2 and not b2) ^ (not a3 and not b3)) and \
    ((not a1 and not c1) ^ (not a2 and not c2) ^ (not a3 and not c3)) and \
    ((not a1 and not e1) ^ (not a2 and not e2) ^ (not a3 and not e3)) and \
    ((not b1 and not d1) ^ (not b2 and not d2) ^ (not b3 and not d3)) and \
    ((not c1 and not e1) ^ (not c2 and not e2) ^ (not c3 and not e3)) and \
    ((not c1 and not d1) ^ (not c2 and not d2) ^ (not c3 and not d3)) and \
    ((not f1 and not d1) ^ (not f2 and not d2) ^ (not f3 and not d3)) and \
    ((not f1 and not e1) ^ (not f2 and not e2) ^ (not f3 and not e3)) and \
    not (not a1 and not a2 and not a3 and not b1 and not b2 and  
         not b3 and not c1 and not c2 and not c3 and \
         not d1 and not d2 and not d3 and not e1 and not e2 and 
         not e3 and not f1 and not f2 and not f3) and \
    (((a1 ^ a2 ^ a3) and not(a1 and a2 and a3)) and ((b1 ^ b2 ^ b3) and not(b1 and b2 and b3)) 
    and ((c1 ^ c2 ^ c3) and not(c1 and c2 and c3)) and ((d1 ^ d2 ^ d3) and not(d1 and d2 and d3))
    and ((e1 ^ e2 ^ e3) and not(e1 and e2 and e3)) and ((f1 ^ f2 ^ f3) and not(f1 and f2 and f3)))
    ) :
        return True
    else : 
        return False