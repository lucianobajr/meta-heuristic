package usecases

import (
	"math"
	"meta-heuristic/app/domain/model"
)

type MetricsService struct {
	Results []float64
}

func NewMetricsService() *MetricsService {
	return &MetricsService{
		Results: make([]float64, 0),
	}
}

func (s *MetricsService) AddResult(result float64) {
	s.Results = append(s.Results, result)
}

func (s *MetricsService) GetMetrics() model.Metrics {
	return model.Metrics{
		Results: s.Results,
	}
}

func Mean(results []float64) float64 {
	sum := 0.0
	for _, r := range results {
		sum += r
	}
	return sum / float64(len(results))
}

func Min(results []float64) float64 {
	min := math.Inf(1)
	for _, r := range results {
		if r < min {
			min = r
		}
	}
	return min
}

func Max(results []float64) float64 {
	max := math.Inf(-1)
	for _, r := range results {
		if r > max {
			max = r
		}
	}
	return max
}

func StandardDeviation(results []float64) float64 {
	mean := Mean(results)
	sumSquares := 0.0
	for _, r := range results {
		sumSquares += math.Pow(r-mean, 2)
	}
	variance := sumSquares / float64(len(results))
	return math.Sqrt(variance)
}
