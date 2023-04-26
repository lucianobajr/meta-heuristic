from metrics.metrics import Metrics
from core.packages.hill_climping import HillClimbing
from core.packages.ils import ILS
from export.export import Export

import numpy as np

if __name__ == "__main__":

    # Executa o algoritmo 30 vezes
    metrics_hc = Metrics()
    metrics_ils = Metrics()
    hill_climbing = HillClimbing(-5, 5, -5, 5,"first")
    export_hill_climbing = Export(metrics_hc,'Boxplot of HC results','Value of objective function','HC')
    export_ils = Export(metrics_ils,'Boxplot of ILS results','Value of objective function','ILS')

    ils = ILS(step_size=1, max_iterations=100, max_restarts=5,type="first")

    for i in range(30):
        result = hill_climbing.heuristic()    
        metrics_hc.insert_result(result)
        solution, value = ils.ils(start_point=(np.random.uniform(-5, 5), np.random.uniform(-5, 5)))
        metrics_ils.insert_result(value)
        
        # print(f"Iteração {i+1}: {result}")
    
    export_hill_climbing.gerenate()
    export_ils.gerenate()