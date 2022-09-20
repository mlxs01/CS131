# s = "Leo will study"
# t = "Peter will study"
# p = "Leo will pass the class"
# q = "Peter will pass the class"

# Both Leo and Peter will study but only one of them 
# will pass the class. Submit a file named p2d.py.

# (s and t) and (p xor q)
# question: is xor not allowed?
(s and t) and ((p or q) and (not(p and q)))
