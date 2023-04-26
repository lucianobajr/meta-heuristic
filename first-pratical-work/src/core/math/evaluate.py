import math
from typing import Union
from abc import ABC, abstractmethod

class IEvaluate:
    @abstractmethod
    def math_evaluate(self, x, y):
        pass

class Evaluate(IEvaluate):
    def __init__(self,type:str) -> None:
        self.type = type

    def math_evaluate(self, x,y):
        if self.type == "first":
            return x**2 + y**2 + 25*(math.sin(x)**2 + math.sin(y)**2)
        elif self.type == "second":
            return -(y+47)*math.sin(math.sqrt(abs(y+0.5*x+47))) - x*math.sin(math.sqrt(abs(x-(y+47))))
            