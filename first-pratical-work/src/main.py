import random
from core.implementations.iterated_local_search import ILS
from core.implementations.hill_climbing import Hill_Climbing

from metrics.metrics import Metrics

if __name__ == "__main__":
    random.seed(42)
    step_size = 0.1
    max_iterations = 1000
   
    ils = ILS(-5, 5, -5, 5, step_size, max_iterations, 50)
    hc = Hill_Climbing(-5,5,-5,5,step_size,max_iterations,50)

    metric_ils = Metrics()
    metrics_hc = Metrics()

    for i in range(30):
        value = ils.heurictic()
        metric_ils.insert_result(value)

        x,y,fx = hc.heurictic()
        metrics_hc.insert_result(fx)
        print("Iteration {}: x = {:.2f}, y = {:.2f}, f(x,y) = {:.2f}".format(i+1, x, y, fx))


    print("\n\nMax ILS: {}; Max HC: {}".format(metric_ils.max(),metrics_hc.max()))