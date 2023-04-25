from hc import HillClimbing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    step_size = 0.1
    max_iterations = 1000
    num_executions = 30
    
    hc = HillClimbing(step_size, max_iterations)
    
    results = []
    for i in range(num_executions):
        start_point = (np.random.uniform(-5, 5), np.random.uniform(-5, 5))
        end_point, value = hc.hill_climbing(start_point)
        results.append(value)
        print(f'{i + 1} - Start point: {start_point}, End point: {end_point}, Value: {value}')
    
    # Generate table
    df = pd.DataFrame({'Value': results})
    table = df.describe()
    print('\n' + str(table))
    
    # Generate boxplot
    fig, ax = plt.subplots()
    ax.boxplot(results, vert=False)
    ax.set_xlabel('Function Value')
    ax.set_yticklabels(['Results'])
    plt.show()