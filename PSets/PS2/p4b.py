# Write a CNF formula in Python using variables x, y, and z that 
# evaluates to 1 if and only if the three variables all have the same value.

not ((x ^ y) or (x ^ z) or (y ^ z))