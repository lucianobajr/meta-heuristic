$ docker build -t meta-heuristic-go .

$ docker run meta-heuristic-go /caminho/do/arquivo

$ go run main.go ./data/*.csv

$ go build -o dist/meta-heuristic-go

$ docker cp <container-id>:/go/src/app/out/image.png .

- base/            (Arquivos e configurações básicas do projeto)
- constants/       (Constantes do projeto)
- core/            (Lógica principal do projeto)
  - math/          (Pacote contendo funcionalidades matemáticas)
  - packages/      (Pacotes utilitários compartilhados)
- domain/          (Camada de domínio do projeto)
  - csv/           (Pacote relacionado à manipulação de arquivos CSV)
  - model/         (Modelos e entidades do domínio)
  - reader/        (Pacote para leitura de dados)
- export/          (Exportação de dados, como geração de relatórios, imagens, etc.)
- use-cases/       (Casos de uso ou interações do sistema)
- utils/           (Utilitários e funções auxiliares)
