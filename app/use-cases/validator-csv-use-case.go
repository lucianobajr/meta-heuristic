package usecases

import csv_domain "meta-heuristic/app/domain/csv"

type ValidatorCSVUseCase struct {
	validatorCSV *csv_domain.ValidatorCSV
}

func NewValidorCSVUseCase(validorCSV *csv_domain.ValidatorCSV) *ValidatorCSVUseCase {
	return &ValidatorCSVUseCase{
		validatorCSV: validorCSV,
	}
}

func (useCase *ValidatorCSVUseCase) ValidateCSVFile(path string) bool {
	return useCase.validatorCSV.ValidatorCSVFile(path)
}
