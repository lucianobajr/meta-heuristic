package utils

import "math/rand"

func RandomFloat(min, max float64) float64 {
	return min + rand.Float64()*(max-min)
}

func GenerateRandomSolution(xLow, xHigh, yLow, yHigh float64) []float64 {
	x := RandomFloat(xLow, xHigh)
	y := RandomFloat(yLow, yHigh)

	result := []float64{x, y}

	return result
}

// Função auxiliar para gerar um passo aleatório baseado no tamanho do passo
func RandomStep(stepSize float64) float64 {
	return (rand.Float64() - 0.5) * stepSize
}
