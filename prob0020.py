# project euler, problem 20

import math

def add(x,y): return str(int(x)+int(y))
print reduce(add, str(math.factorial(100)))
