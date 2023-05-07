build:
	go build -o dist/meta-heuristic-go 
dev:
	go run main.go ./data/b.csv
run:
	./dist/meta-heuristic-go  ./data/b.csv