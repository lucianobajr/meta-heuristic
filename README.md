# Meta-Heuristic

## Executar Projeto

### Rodar
    $ go run main.go ./data/*.csv

### Gerar build
    $ go build -o dist/meta-heuristic-go

## Docker

### Criar imagem docker

    $ docker build -t meta-heuristic-go .

### Criar imagem docker

    $ docker run meta-heuristic-go /caminho/do/arquivo

## Copiar a image.png gerada para um diretório

    $ docker cp <container-id>:/go/src/app/out/image.png .

## Structure Folder

    ├── base/            (Arquivos e configurações básicas do projeto)
    ├── constants/       (Constantes do projeto)
    ├── core/            (Lógica principal do projeto)
    │  ├── math/          (Pacote contendo funcionalidades matemáticas)
    │  ├── packages/      (Pacotes utilitários compartilhados)
    ├── domain/          (Camada de domínio do projeto)
    │  ├── csv/           (Pacote relacionado à manipulação de arquivos CSV)
    │  ├── model/         (Modelos e entidades do domínio)
    │  ├── reader/        (Pacote para leitura de dados)
    ├── export/          (Exportação de dados, como geração de relatórios, imagens, etc.)
    ├── use-cases/       (Casos de uso ou interações do sistema)
    ├── utils/           (Utilitários e funções auxiliares)
    │   