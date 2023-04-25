import math

class Metrics:
    def __init__(self) -> None:
        self.results = list()

    def insert_result(self,value):
        self.results.append(value)

    def min(self):
        return min(self.results)
    
    def max(self):
        return max(self.results)

    def mean(self):
        return sum(self.results)/len(self.results)
    
    def standard_deviation(self):
        total_sum = sum((x - self.mean()) ** 2 for x in self.results)
        varience = (total_sum / len(self.results))
        
        return math.sqrt(varience)