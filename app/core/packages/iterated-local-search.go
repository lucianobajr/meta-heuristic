package packages

import (
	"math/rand"
	"meta-heuristic/app/core/math"
	"meta-heuristic/app/domain/reader"
	"meta-heuristic/app/utils"
)

func IteratedLocalSearch(data *reader.DataCSV) float64 {
	// Geração da solução inicial
	initialSolution := generateRandomSolution(data.XLow, data.XHight, data.YLow, data.YHight)
	bestSolution := initialSolution

	// Configuração dos parâmetros do algoritmo
	maxIterations := 100
	perturbationFactor := 0.1

	evaluateService := &math.EvaluateService{}

	// Cálculo do objetivo da melhor solução inicial
	bestObjective := evaluateService.CalculateObjective(data.Evaluate, bestSolution[0], bestSolution[1])

	for i := 0; i < maxIterations; i++ {
		// Busca local
		localSolution := localSearch(bestSolution, data)

		// Perturbação
		perturbedSolution := perturb(localSolution, perturbationFactor, data)

		// Busca local na solução perturbada
		localSolutionPerturbed := localSearch(perturbedSolution, data)

		// Cálculo do objetivo da solução perturbada
		perturbedObjective := evaluateService.CalculateObjective(data.Evaluate, localSolutionPerturbed[0], localSolutionPerturbed[1])

		// Atualização da melhor solução
		if perturbedObjective < bestObjective {
			bestSolution = localSolutionPerturbed
			bestObjective = perturbedObjective
		}
	}

	return bestObjective
}

func generateRandomSolution(xLow, xHigh, yLow, yHigh float64) []float64 {
	x := utils.RandomFloat(xLow, xHigh)
	y := utils.RandomFloat(yLow, yHigh)

	result := []float64{x, y}

	return result
}

func localSearch(solution []float64, data *reader.DataCSV) []float64 {
	bestSolution := solution

	maxIterations := 10

	evaluateService := &math.EvaluateService{}

	for i := 0; i < maxIterations; i++ {
		perturbedSolution := perturb(bestSolution, 0.1, data)

		// Verifica se a solução perturbada é melhor do que a atual
		if evaluateService.CalculateObjective(data.Evaluate, perturbedSolution[0], perturbedSolution[1]) < evaluateService.CalculateObjective(data.Evaluate, bestSolution[0], bestSolution[1]) {
			bestSolution = perturbedSolution
		}
	}

	return bestSolution
}

func perturb(solution []float64, perturbationFactor float64, data *reader.DataCSV) []float64 {
	perturbedX := perturbCoordinate(solution[0], perturbationFactor, data.XLow, data.XHight)
	perturbedY := perturbCoordinate(solution[1], perturbationFactor, data.YLow, data.YHight)
	return []float64{perturbedX, perturbedY}
}

func perturbCoordinate(coordinate, perturbationFactor, low, high float64) float64 {
	perturbation := perturbationFactor * (rand.Float64() - 0.5)
	perturbedCoordinate := coordinate + perturbation

	// Verifica se o valor perturbado está dentro dos limites
	if perturbedCoordinate < low {
		perturbedCoordinate = low
	} else if perturbedCoordinate > high {
		perturbedCoordinate = high
	}

	return perturbedCoordinate
}
