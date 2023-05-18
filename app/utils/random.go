package utils

import (
	"math/rand"
	"meta-heuristic/app/domain/model"
)

// gera um número aleatório do tipo float64 dentro de um intervalo especificado.
func RandomFloat(min, max float64) float64 {
	return min + rand.Float64()*(max-min)
}

func GenerateRandomSolution(xLow, xHigh, yLow, yHigh float64) model.SolutionState {
	x := RandomFloat(xLow, xHigh)
	y := RandomFloat(yLow, yHigh)

	return model.SolutionState{
		X: x,
		Y: y,
	}
}

// Função auxiliar para gerar um passo aleatório baseado no tamanho do passo
func RandomStep(stepSize float64) float64 {
	return (rand.Float64() - 0.5) * stepSize
}
