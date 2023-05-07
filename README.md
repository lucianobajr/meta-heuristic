# Meta-Heuristic

## ILS 

A meta-heurística Iterated Local Search (ILS) é um algoritmo de busca heurística que combina a busca local com uma perturbação aleatória para encontrar soluções melhores em problemas de otimização. Ela é especialmente útil em problemas onde a busca local tradicional pode ficar presa em ótimos locais subótimos.

A ILS é uma técnica iterativa que realiza uma busca local repetidamente com pequenas perturbações aleatórias nas soluções encontradas. O objetivo é escapar de ótimos locais subótimos e explorar regiões de busca mais amplas.

Aqui está uma visão geral do funcionamento da ILS:

Geração da solução inicial: A ILS começa gerando uma solução inicial para o problema. Essa solução pode ser obtida de várias maneiras, como aleatoriamente, com heurísticas construtivas ou por meio de outras técnicas.

Busca local: A partir da solução inicial, é aplicada uma busca local para melhorar essa solução. A busca local explora as vizinhanças da solução atual e realiza movimentos locais para encontrar uma solução de melhor qualidade dentro dessa vizinhança. O objetivo é chegar a um ótimo local, mas pode haver situações em que a busca local fique presa em um ótimo local subótimo.

Perturbação: Após a busca local, é aplicada uma perturbação aleatória à solução encontrada. Essa perturbação introduz mudanças na solução atual para explorar diferentes regiões de busca. Essas mudanças podem ser feitas de forma aleatória ou seguindo alguma lógica específica do problema.

Busca local na nova solução: A partir da solução perturbada, é realizada novamente uma busca local para melhorar essa nova solução. A busca local é aplicada em um espaço de busca menor do que a busca original, pois parte da solução atual já foi explorada.

Critério de parada: O processo de busca local e perturbação é repetido por um número fixo de iterações ou até que um critério de parada seja satisfeito. O critério de parada pode ser um número máximo de iterações, um limite de tempo ou alguma condição específica do problema.

Retorno da melhor solução encontrada: Após o término das iterações, a ILS retorna a melhor solução encontrada durante todo o processo de busca.

A ILS pode ser ajustada e adaptada para diferentes problemas e contextos, incorporando estratégias específicas de perturbação, vizinhança e busca local de acordo com as características do problema em questão.

É importante ressaltar que a ILS é uma meta-heurística e não garante a obtenção da melhor solução global para um problema de otimização. No entanto, ela é capaz de explorar diferentes regiões de busca e fornecer soluções de alta qualidade em muitos casos.

## Hill Climbing


A meta-heurística Hill Climbing, também conhecida como escalada de colina, é um algoritmo de otimização que busca encontrar a melhor solução em um espaço de busca. Essa heurística é baseada em um princípio simples: "subir a colina", ou seja, fazer movimentos que levem a uma melhoria incremental da solução atual.

O funcionamento básico do Hill Climbing é o seguinte:

Inicialização: Começamos com uma solução inicial, que pode ser gerada aleatoriamente ou definida de alguma outra forma.

Avaliação: Calculamos uma medida de qualidade para a solução atual. Essa medida é chamada de função objetivo ou função de avaliação. Ela determina o quão boa é a solução em termos de otimização.

Vizinhança: Geramos soluções vizinhas à solução atual. Uma solução vizinha é obtida através de uma pequena modificação na solução atual. Essas modificações podem ser feitas de várias maneiras, dependendo do problema em questão.

Movimento: Selecionamos a melhor solução entre as soluções vizinhas com base na função objetivo. Se uma solução vizinha é melhor do que a solução atual, fazemos o movimento para essa solução e a tornamos a nova solução atual. Caso contrário, encerramos o algoritmo, pois consideramos que encontramos um ótimo local.

Repetição: Os passos 2 a 4 são repetidos até que uma condição de parada seja atingida. Essa condição pode ser um número máximo de iterações, uma melhoria mínima da solução ou qualquer outro critério definido.

O Hill Climbing é um algoritmo de busca local, o que significa que ele pode ficar preso em ótimos locais, não conseguindo encontrar a melhor solução global. Isso ocorre porque o algoritmo só faz movimentos com base na melhoria local imediata, sem considerar movimentos que possam levar a melhorias a longo prazo.

Existem variantes do Hill Climbing que tentam contornar esse problema, como o Hill Climbing Estocástico, que aceita movimentos que pioram a solução atual em uma certa probabilidade, e o Hill Climbing com Reinício Aleatório, que realiza múltiplas execuções a partir de diferentes soluções iniciais.

Em resumo, o Hill Climbing é um algoritmo simples, mas eficaz, para encontrar soluções em problemas de otimização. Ele é fácil de implementar e entender, mas pode ficar preso em ótimos locais. É importante ajustar os parâmetros e considerar variantes do algoritmo para melhorar sua eficiência e capacidade de encontrar soluções ótimas.


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

## APP Structure Folder

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