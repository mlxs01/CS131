from ast import Or
from operator import xor


s = "Leo will study"
t = "Peter will study"
p = "Leo will pass the class"
q = "Peter will pass the class"

# Leo will study or he will not pass the 
# class. Submit a file named p2b.py.

s or not(p)
# recheck this one ^ DO THIS BY USING TRUTH TABLE