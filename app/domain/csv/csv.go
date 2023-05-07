package csv

import (
	"encoding/csv"
	file_fields_constants "meta-heuristic/app/constants"
	"os"
	"strings"
)

type ValidatorCSV struct{}

func (v *ValidatorCSV) ValidatorCSVFile(path string) bool {
	if !strings.HasSuffix(path, ".csv") {
		return false
	}

	file, err := os.Open(path)

	if err != nil {
		return false
	}

	defer file.Close()

	reader := csv.NewReader(file)
	columns, err := reader.Read()

	if err != nil {
		return false
	}

	requiredFields := file_fields_constants.FileFields

	for _, field := range requiredFields {
		if !containsField(columns, field) {
			return false
		}
	}

	return true
}

func containsField(columns []string, field string) bool {
	for _, c := range columns {
		if c == field {
			return true
		}
	}

	return false
}
