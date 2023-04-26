from core.math.evaluate import Evaluate
import random

class HillClimbing:
    def __init__(self,x_low, x_high, y_low, y_high, type:str) -> None:
        self.x_low = x_low
        self.x_high = x_high
        self.y_low = y_low
        self.y_high = y_high
        self.evalute = Evaluate(type)

    def heuristic(self):

        # Inicializa o estado atual
        x_current = random.uniform(self.x_low, self.x_high)
        y_current = random.uniform(self.y_low, self.y_high)

        current = self.evalute.math_evaluate(x_current, y_current)
        
        # Loop principal
        while True:
            # Gera um novo estado vizinho
            x_new = random.uniform(self.x_low, self.x_high)
            y_new = random.uniform(self.y_low, self.y_high)
            neighbor = self.evalute.math_evaluate(x_new, y_new)
            
            # Aceita o novo estado se ele for melhor que o atual
            if neighbor < current:
                x_current, y_current = x_new, y_new
                current = neighbor
            
            # Se o algoritmo atingiu um mínimo local, retorna o valor atual
            else:
                return current