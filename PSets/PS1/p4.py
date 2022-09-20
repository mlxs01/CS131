# c = "Christian feels better by the weekend"
# a = "Anna wants to go swimming"
# b = "Benjiamin wants to go swimming"
# d = "Diana wants to go swimming"
# T = "if Christian feels better by the weekend and 
# if the majority of Anna, Benjamin, and Diana want to go swimming."

# would this work v
# no becuase if c is False, then everything clapses 
c and ((a and b) or (a and d) or (b and d))
# a=True b=True c=False d=False

