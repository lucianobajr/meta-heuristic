package packages

import (
	"meta-heuristic/app/core/math"
	"meta-heuristic/app/domain/model"
	"meta-heuristic/app/domain/reader"
	"meta-heuristic/app/utils"
)

func IteratedLocalSearch(data *reader.DataCSV) float64 {
	// Geração da solução inicial
	initialSolution := utils.GenerateRandomSolution(data.XLow, data.XHight, data.YLow, data.YHight)
	bestSolution := initialSolution

	// Configuração dos parâmetros do algoritmo
	maxIterations := 100
	perturbationFactor := 0.1

	evaluateService := &math.EvaluateService{}

	// Cálculo do objetivo da melhor solução inicial
	bestObjective := evaluateService.CalculateObjective(data.Evaluate, bestSolution.X, bestSolution.Y)

	for i := 0; i < maxIterations; i++ {
		// Busca local
		localSolution := localSearch(bestSolution, data)

		// Perturbação
		perturbedSolution := perturb(localSolution, perturbationFactor, data)

		// Busca local na solução perturbada
		localSolutionPerturbed := localSearch(perturbedSolution, data)

		// Cálculo do objetivo da solução perturbada
		perturbedObjective := evaluateService.CalculateObjective(data.Evaluate, localSolutionPerturbed.X, localSolutionPerturbed.Y)

		// Atualização da melhor solução
		if perturbedObjective < bestObjective {
			bestSolution = localSolutionPerturbed
			bestObjective = perturbedObjective
		}
	}

	return bestObjective
}

func localSearch(solution model.SolutionState, data *reader.DataCSV) model.SolutionState {
	bestSolution := solution

	maxIterations := 10

	evaluateService := &math.EvaluateService{}

	for i := 0; i < maxIterations; i++ {
		perturbedSolution := perturb(bestSolution, 0.1, data)

		// Verifica se a solução perturbada é melhor do que a atual
		if evaluateService.CalculateObjective(data.Evaluate, perturbedSolution.X, perturbedSolution.Y) < evaluateService.CalculateObjective(data.Evaluate, bestSolution.X, bestSolution.Y) {
			bestSolution = perturbedSolution
		}
	}

	return bestSolution
}

func perturb(solution model.SolutionState, perturbationFactor float64, data *reader.DataCSV) model.SolutionState {
	perturbedX := perturbCoordinate(solution.X, perturbationFactor, data.XLow, data.XHight)
	perturbedY := perturbCoordinate(solution.Y, perturbationFactor, data.YLow, data.YHight)
	return model.SolutionState{
		X: perturbedX,
		Y: perturbedY,
	}

}

func perturbCoordinate(coordinate, perturbationFactor, low, high float64) float64 {
	perturbation := utils.RandomStep(perturbationFactor)
	perturbedCoordinate := coordinate + perturbation

	// Verifica se o valor perturbado está dentro dos limites
	if perturbedCoordinate < low {
		perturbedCoordinate = low
	} else if perturbedCoordinate > high {
		perturbedCoordinate = high
	}

	return perturbedCoordinate
}
