from core.math.first_evaluate import evaluate
import random

class ILS:
    def __init__(self, x_min:int , x_max:int, y_min:int, y_max:int, neighborhood_size:int, max_iterations:int, max_iterations_without_improvement:int) -> None:
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.neighborhood_size = neighborhood_size
        self.max_iterations = max_iterations
        self.max_iterations_without_improvement = max_iterations_without_improvement

    def heurictic(self):
        # Definir a solução inicial aleatória
        x0 = random.uniform(self.x_min, self.x_max)
        y0 = random.uniform(self.y_min, self.y_max)
        best_x, best_y = x0, y0
        best_score = float('inf')

        # Iniciar o loop principal
        iterations_without_improvement = 0
        for i in range(self.max_iterations):
            # Gerar uma solução na vizinhança da solução atual
            x1 = x0 + random.uniform(-self.neighborhood_size,self.neighborhood_size)
            y1 = y0 + random.uniform(-self.neighborhood_size, self.neighborhood_size)

            # Verificar se a nova solução está dentro dos limites dos intervalos
            x1 = max(self.x_min, min(x1, self.x_max))
            y1 = max(self.y_min, min(y1, self.y_max))

            # Calcular a pontuação da nova solução
            score = evaluate(x1, y1)

            # Verificar se a nova solução é melhor do que a melhor solução atual
            if score < best_score:
                best_score = score
                best_x, best_y = x1, y1
                iterations_without_improvement = 0
            else:
                iterations_without_improvement += 1

            # Verificar se ultrapassou o número máximo de iterações sem melhora
            if iterations_without_improvement >= self.max_iterations_without_improvement:
                # Reiniciar a solução aleatória
                x0 = random.uniform(self.x_min, self.x_max)
                y0 = random.uniform(self.y_min, self.y_max)
                iterations_without_improvement = 0
            else:
                # Configurar a nova solução como a solução atual
                x0 = x1
                y0 = y1

        # Imprimir a melhor solução encontrada
        print(f"Melhor solução[ILS]: f({best_x:.4f}, {best_y:.4f}) = {best_score:.4f}")

        return best_score