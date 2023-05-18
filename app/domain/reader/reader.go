package reader

import (
	"encoding/csv"
	"errors"
	"fmt"
	"os"
	"strconv"
)

type ReaderCSV struct{}

type DataCSV struct {
	Evaluate string
	XLow     float64
	XHigh    float64
	YLow     float64
	YHigh    float64
}

func (r *ReaderCSV) ReadCSVFile(path string) (*DataCSV, error) {
	file, err := os.Open(path)

	if err != nil {
		return nil, err
	}

	defer file.Close()

	reader := csv.NewReader(file)
	lines, err := reader.ReadAll()

	if err != nil {
		return nil, err
	}

	if len(lines) != 2 {
		return nil, errors.New("O arquivo CSV não contém dados suficientes")
	}

	if !validateEvaluate(lines[1][0]) {
		return nil, errors.New("O campo 'evaluate' deve ser 'first' ou 'second'")
	}

	values, err := castStringToInt(lines[1][1:])

	if err != nil {
		return nil, err
	}

	data := &DataCSV{
		Evaluate: lines[1][0],
		XLow:     values[0],
		XHigh:    values[1],
		YLow:     values[2],
		YHigh:    values[3],
	}

	return data, nil
}

func validateEvaluate(evaluate string) bool {
	return evaluate == "first" || evaluate == "second"
}

func castStringToInt(data []string) ([]float64, error) {
	var finalData []float64

	for _, value := range data {
		finalValue, err := strconv.ParseFloat(value, 64)
		if err != nil {
			fmt.Println("Erro ao converter XLow para int64:", err)
			return nil, err
		}

		finalData = append(finalData, finalValue)
	}

	return finalData, nil
}
