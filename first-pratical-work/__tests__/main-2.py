# main.py

import numpy as np
import matplotlib.pyplot as plt

from typing import List, Tuple
import math
from prettytable import PrettyTable


class ILS:
    def __init__(self, step_size: float, max_iterations: int, max_restarts: int):
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.max_restarts = max_restarts
        
    def evaluate_function(self, x: float, y: float) -> float:
        return x**2 + y**2 + 25 * (math.sin(x)**2 + math.sin(y)**2)

    def ils(self, start_point: Tuple[float, float]) -> Tuple[float, float]:
        best_solution = start_point
        best_value = self.evaluate_function(*start_point)
        current_solution = start_point
        current_value = best_value
        num_iterations = 0
        num_restarts = 0

        while num_restarts < self.max_restarts:
            candidate_solution = self.perturb_solution(current_solution)
            candidate_value = self.evaluate_function(*candidate_solution)
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
            candidate_value = self.evaluate_function(*candidate_solution)
            num_iterations += 1

            if candidate_value < current_value:
                current_solution, current_value = candidate_solution, candidate_value
        
        return current_solution, current_value

def run_ils(num_runs: int) -> np.ndarray:
    ils = ILS(step_size=1, max_iterations=100, max_restarts=5)
    results = np.zeros(num_runs)

    for i in range(num_runs):
        solution, value = ils.ils(start_point=(np.random.uniform(-5, 5), np.random.uniform(-5, 5)))
        results[i] = value

    return results

if __name__ == '__main__':
    num_runs = 30
    results = run_ils(num_runs)

    print(f'Mean: {results.mean()}')
    print(f'Minimum value: {results.min()}')
    print(f'Maximum value: {results.max()}')
    print(f'Standard deviation: {results.std()}')

    from prettytable import PrettyTable

    # Criar a tabela
    table = PrettyTable()
    table.field_names = ["Mean", "Min", "Max","STD"]

    # Adicionar dados à tabela
    table.add_row([results.mean(),results.min(),results.max(),results.std()])

    # Imprimir a tabela
    print(table)

    
    fig, ax = plt.subplots()
    ax.boxplot(results)
    ax.set_title('Boxplot of ILS results')
    ax.set_ylabel('Value of objective function')
    
    fig.savefig('../out/boxplot.png')
