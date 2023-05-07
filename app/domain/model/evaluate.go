package model

type EvaluateRepository interface {
	CalculateObjective(x, y float64) float64
}

type Evaluate struct {
	X, Y float64
}
