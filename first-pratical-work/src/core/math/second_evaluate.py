import math

def evaluate(x, y):
    return -(y+47)*math.sin(math.sqrt(abs(y+0.5*x+47))) - x*math.sin(math.sqrt(abs(x-(y+47))))