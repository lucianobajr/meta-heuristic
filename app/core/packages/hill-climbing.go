package packages

import (
	"meta-heuristic/app/core/math"
	"meta-heuristic/app/domain/model"
	"meta-heuristic/app/domain/reader"
	"meta-heuristic/app/utils"
)

func HillClimbingOptimization(data *reader.DataCSV) float64 {
	// Configuração dos parâmetros do algoritmo
	maxIterations := 100
	stepSize := 0.1

	// Inicialização do estado da solução
	initialState := model.SolutionState{
		X: utils.RandomFloat(data.XLow, data.XHight),
		Y: utils.RandomFloat(data.YLow, data.YHight),
	}

	evaluateService := &math.EvaluateService{}

	currentState := initialState
	bestObjective := evaluateService.CalculateObjective(data.Evaluate, currentState.X, currentState.Y)

	// Inicialização do gerador de números aleatórios

	// Loop principal do algoritmo
	for i := 0; i < maxIterations; i++ {
		// Geração do próximo estado
		nextState := model.SolutionState{
			X: currentState.X + utils.RandomStep(stepSize),
			Y: currentState.Y + utils.RandomStep(stepSize),
		}

		// Avaliação do próximo estado
		nextObjective := evaluateService.CalculateObjective(data.Evaluate, nextState.X, nextState.Y)

		// Verificação se o próximo estado é melhor
		if nextObjective < bestObjective {
			bestObjective = nextObjective
		}

		// Atualização do estado atual
		currentState = nextState
	}

	return bestObjective
}
