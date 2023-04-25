import random
from core.math.first_evaluate import evaluate

class Hill_Climbing:
    def __init__(self, x_min:int , x_max:int, y_min:int, y_max:int, step_size:int, max_iterations:int, max_iterations_without_improvement:int) -> None:
        self.start_x = random.uniform(x_min, x_max)
        self.start_y = random.uniform(y_min, y_max)
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.max_iterations_without_improvement = max_iterations_without_improvement

    def heurictic(self):
        x = self.start_x
        y = self.start_y
        fx = evaluate(x, y)
        
        for i in range(self.max_iterations):
            neighbors = [(x + self.step_size, y), (x - self.step_size, y), (x, y + self.step_size), (x, y - self.step_size)]
            neighbor_values = [evaluate(neighbor[0], neighbor[1]) for neighbor in neighbors]
            min_neighbor_value = min(neighbor_values)
            
            if min_neighbor_value < fx:
                best_neighbors = [neighbors[i] for i in range(len(neighbors)) if neighbor_values[i] == min_neighbor_value]
                x, y = random.choice(best_neighbors)
                fx = min_neighbor_value
            else:
                return x, y, fx
            
        return x, y, fx