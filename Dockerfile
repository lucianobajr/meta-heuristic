# Use uma imagem base com o Go instalado
FROM golang:latest

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /go/src/app

# Copie o arquivo go.mod e go.sum para o diretório de trabalho
COPY go.mod go.sum ./

# Baixe as dependências do projeto
RUN go mod download

# Copie o código-fonte para o diretório de trabalho
COPY . .

# Construa o aplicativo
RUN go build -o meta-heuristic-go

# Defina o comando padrão para executar o aplicativo
CMD ["./meta-heuristic-go"]
ENTRYPOINT ["./meta-heuristic-go"]