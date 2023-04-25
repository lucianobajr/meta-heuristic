from typing import List, Tuple
import math

class HillClimbing:
    def __init__(self, step_size: float, max_iterations: int):
        self.step_size = step_size
        self.max_iterations = max_iterations
        
    def evaluate_function(self, x: float, y: float) -> float:
        return x**2 + y**2 + 25 * (math.sin(x)**2 + math.sin(y)**2)

    def hill_climbing(self, start_point: Tuple[float, float]) -> Tuple[float, float]:
        current_point = start_point
        current_value = self.evaluate_function(*current_point)

        for i in range(self.max_iterations):
            neighbors = self.generate_neighbors(current_point, self.step_size)
            next_point = max(neighbors, key=lambda point: self.evaluate_function(*point))
            next_value = self.evaluate_function(*next_point)

            if next_value < current_value:
                current_point, current_value = next_point, next_value
            else:
                break

        return current_point, current_value

    def generate_neighbors(self, point: Tuple[float, float], step_size: float) -> List[Tuple[float, float]]:
        x, y = point
        neighbors = []
        for dx in [-step_size, 0, step_size]:
            for dy in [-step_size, 0, step_size]:
                if dx == dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                if -5 <= new_x <= 5 and -5 <= new_y <= 5:
                    neighbors.append((new_x, new_y))
        return neighbors