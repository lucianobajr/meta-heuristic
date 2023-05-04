import random
from math import sin

def f(x, y):
    return x**2 + y**2 + 25*(sin(x)**2 + sin(y)**2)

def perturbation(x, y, step):
    new_x = x + random.uniform(-step, step)
    new_y = y + random.uniform(-step, step)
    return new_x, new_y

def ils(x_low, x_high, y_low, y_high):
    # Passo 1: Gere uma solução inicial aleatória
    x = random.uniform(x_low, x_high)
    y = random.uniform(y_low, y_high)
    s = f(x, y)
    
    # Passo 2: Repita até que o critério de parada seja atendido
    while True:
        # Passo 3: Realize uma perturbação na solução atual
        x_new, y_new = perturbation(x, y, 0.1)
        s_new = f(x_new, y_new)
        
        # Passo 4: Execute a busca local na nova solução
        for i in range(10):
            x_new, y_new = perturbation(x, y, 0.1)
            s_i = f(x_new, y_new)
            if s_i < s_new:
                x_new_best, y_new_best = x_new, y_new
                s_new = s_i
        
        # Passo 5: Aceite a nova solução com probabilidade p
        if s_new < s:
            x, y, s = x_new_best, y_new_best, s_new
        else:
            p = random.uniform(0, 1)
            if p < 0.5:
                x, y = x_new, y_new
        
        # Passo 6: Cheque o critério de parada
        if s < 1e-6:
            break
    
    # Retorne a melhor solução encontrada
    return x, y, s

# exemplo de uso
results = []
for i in range(30):
    x, y, s = ils(-5, 5, -5, 5)
    results.append(s)
    print(f"Iteration {i+1}: x = {x}, y = {y}, f(x, y) = {s}")

# tabela de resultados
print("Results summary:")
print(f"Mean: {sum(results)/len(results)}")
print(f"Minimum: {min(results)}")
print(f"Maximum: {max(results)}")
import statistics
print(f"Standard deviation: {statistics.stdev(results)}")
