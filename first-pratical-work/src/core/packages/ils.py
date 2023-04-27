from core.math.evaluate import Evaluate

from typing import Tuple
import numpy as np

class ILS:
    def __init__(self, step_size: float, max_iterations: int, max_restarts: int, x_low, x_high, y_low, y_high,type: str):
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.max_restarts = max_restarts
        self.x_low = x_low
        self.x_high = x_high
        self.y_low = y_low
        self.y_high = y_high
        self.evalute = Evaluate(type)

    def heuristic(self) -> Tuple[float, float]:
        start_point = (np.random.uniform(self.x_low, self.x_high), np.random.uniform(self.y_low, self.y_high))
        
        best_solution = start_point
        best_value = self.evalute.math_evaluate(start_point[0],start_point[1])
        current_solution = start_point
        current_value = best_value
        num_iterations = 0
        num_restarts = 0

        while num_restarts < self.max_restarts:
            candidate_solution = self.perturb_solution(current_solution)
            candidate_value = self.evalute.math_evaluate(candidate_solution[0],candidate_solution[1])
            candidate_solution, candidate_value = self.local_search(candidate_solution, candidate_value)
            num_iterations += self.max_iterations

            if candidate_value < best_value:
                best_solution, best_value = candidate_solution, candidate_value
            
            current_solution, current_value = candidate_solution, candidate_value
            num_restarts += 1
        
        return best_solution, best_value

    def perturb_solution(self, point: Tuple[float, float]) -> Tuple[float, float]:
        x, y = point
        new_x = np.clip(x + np.random.uniform(-self.step_size, self.step_size), -5, 5)
        new_y = np.clip(y + np.random.uniform(-self.step_size, self.step_size), -5, 5)
        return (new_x, new_y)

    def local_search(self, start_point: Tuple[float, float], start_value: float) -> Tuple[float, float]:
        current_solution = start_point
        current_value = start_value
        num_iterations = 0

        while num_iterations < self.max_iterations:
            candidate_solution = self.perturb_solution(current_solution)
            candidate_value = self.evalute.math_evaluate(candidate_solution[0],candidate_solution[1])
            num_iterations += 1

            if candidate_value < current_value:
                current_solution, current_value = candidate_solution, candidate_value
        
        return current_solution, current_value