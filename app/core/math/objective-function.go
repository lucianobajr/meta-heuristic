package math

import (
	"math"
	_ "meta-heuristic/app/domain/model"
)

type EvaluateService struct{}

func (s *EvaluateService) CalculateObjective(param string, x, y float64) float64 {
	// Lógica de cálculo da função objetivo
	// baseado no parâmetro fornecido ("first" ou "second")
	if param == "first" {
		return s.calculateFirstObjective(x, y)
	} else if param == "second" {
		return s.calculateSecondObjective(x, y)
	} else {
		// Lidar com um parâmetro inválido aqui
		return 0
	}
}

func (s *EvaluateService) calculateFirstObjective(x, y float64) float64 {
	return x*x + y*y + 25*(math.Pow(math.Sin(x), 2)+math.Pow(math.Sin(y), 2))
}

func (s *EvaluateService) calculateSecondObjective(x, y float64) float64 {
	return -(y+47)*math.Sin(math.Sqrt(math.Abs(y+0.5*x+47))) - x*math.Sin(math.Sqrt(math.Abs(x-(y+47))))
}

type EvaluateRepository struct {
	Service *EvaluateService
}

func NewEvaluateRepository() *EvaluateRepository {
	return &EvaluateRepository{
		Service: &EvaluateService{},
	}
}

func (r *EvaluateRepository) CalculateObjective(param string, x, y float64) float64 {
	return r.Service.CalculateObjective(param, x, y)
}
