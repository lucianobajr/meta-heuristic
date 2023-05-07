package usecases

import "meta-heuristic/app/domain/reader"

type ReaderCSVUseCase struct {
	reader *reader.ReaderCSV
}

func NewReaderCSVUseCase(readerCSV *reader.ReaderCSV) *ReaderCSVUseCase {
	return &ReaderCSVUseCase{
		reader: readerCSV,
	}
}

func (useCase *ReaderCSVUseCase) ReadCSVFile(path string) (*reader.DataCSV, error) {
	return useCase.reader.ReadCSVFile(path)
}
