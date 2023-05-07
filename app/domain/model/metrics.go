package model

type MetricsRepository interface {
	AddResult(result float64)
	GetMetrics() Metrics
}

type Metrics struct {
	Results []float64
}
