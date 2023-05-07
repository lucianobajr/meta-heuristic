package base

import (
	"log"
	"math/rand"
	"os"
	"time"

	"meta-heuristic/app/core/packages"
	csv_domain "meta-heuristic/app/domain/csv"
	"meta-heuristic/app/domain/reader"
	"meta-heuristic/app/export"
	usecases "meta-heuristic/app/use-cases"
)

func run(path string) {
	validator := &csv_domain.ValidatorCSV{}
	validatorUseCase := usecases.NewValidorCSVUseCase(validator)

	if !validatorUseCase.ValidateCSVFile(path) {
		log.Fatal("Arquivo inválido!")
	}

	reader := &reader.ReaderCSV{}
	readerUseCase := usecases.NewReaderCSVUseCase(reader)

	data, err := readerUseCase.ReadCSVFile(path)

	if err != nil {
		log.Fatal(err)
	}

	//evaluateService := &math.EvaluateService{}
	//fmt.Println(evaluateService.CalculateObjective(data.Evaluate, 2.0, 3.0))

	rand.Seed(time.Now().UnixNano())

	metricsServiceILS := usecases.NewMetricsService()
	metricsServiceHC := usecases.NewMetricsService()

	iterations := 30
	for i := 0; i < iterations; i++ {
		//fmt.Printf("Execução %d:\n", i+1)

		metricsServiceILS.AddResult(packages.IteratedLocalSearch(data))
		metricsServiceHC.AddResult(packages.HillClimbingOptimization(data))

		//fmt.Println("Valor da função objetivo:", objectiveValues[i])
		//fmt.Println()
	}

	export.Export(metricsServiceILS)
	export.Export(metricsServiceHC)
}

func Bootstrap() {
	if len(os.Args) < 2 {
		log.Fatal("Você deve fornecer o caminho do arquivo como argumento.")
	}

	run(os.Args[1])
}
