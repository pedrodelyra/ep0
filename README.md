## EP0 - Desenvolvimento Avançado de Software

###### Alunos: Iago Rodrigues, Lucas Mattioli e Pedro de Lyra
###### Professores: Fábio Mendes e Paulo Meirelles

A proposta do trabalho é a implementação de um software que envolva múltiplos padrões de projeto. Nosso sistema foi escrito em Python e possui como objetivo implementar formas de se encontrar a distância com o menor custo entre dois locais.

Para que isso fosse possível, implementou-se em primeiro lugar a classe Graph que abstrai um grafo. Um grafo pode ser entendido como uma estrutura matemática que consiste em um conjunto de elementos e um conjunto de pares ordenados que representam algum tipo de relação entre dois vértices. Para implementar esta estrutura em código, foi usado uma estrutura fornecida pela biblioteca padrão do python, o dict, cuja implementação por baixo dos panos é uma hash table. O dict foi utilizado para implementar uma lista de adjacências representando os elementos do grafo e seus respectivos relacionamentos (que consistem em pares indicando o elemento vizinho e o custo daquela conexão). O grafo possui também uma estratégia de travessia, isto é, um atributo que armazena qual algoritmo será utilizado para determinar as distâncias entre um vértice de origem e o restante dos vértices do grafo. A classe Graph conta com 8 métodos:
* **__init__**: este método é o construtor do grafo e apenas inicia seus atributos, uma lista de adjacências, sua estratégia de travessia e um atributo auxiliar que conta o número de vértices visitados quando o grafo é iterado.
* **choose_traversal_strategy**: este método seleciona a estratégia de travessia do grafo, ou seja, qual algoritmo será utilizado para computar o menor caminho entre uma origem e os outros vértices do grafo. Atualmente o sistema conta com três estratégias disponíveis: Bellman-Ford, Dijkstra e Floyd-Warshall.
* **traverse_from_source**: Este método computa a distância entre um vértice de origem e o restante dos vértices do grafo.
* **add_unidirectional_edge/add_bidirectional_edge**: Adiciona uma aresta unidirecional ou bidirecional, respectivamente, representando uma relação entre dois vértices.
* **__str__**: retorna uma representação em string do grafo (uma lista de vértices e seus respectivos vizinhos).
* **__iter__/__next__**: métodos utilizados para tornar uma instância da classe Grafo iterável.

#### Padrões de Projeto implementados
1. **Iterator**: a implementação deste padrão aproveitou de recursos fornecidos pelo próprio python. É possível tornar um objeto iterável desde que dois métodos sejam implementados por sua classe: **__iter__** para determinar o ponto de partida da iteração e **__next__** para indicar o próximo elemento da iteração ou se não existem mais elementos.

2. **Strategy**: como já foi explicado anteriormente, a classe grafo possui múltiplas estratégias de travessia. Para implementar este sistema de estratégias foi utilizado o padrão Strategy. Um grafo possui uma estratégia de travessia, e uma estratégia de travessia dentro do sistema é implementada através de uma classe que herda da classe TraversalStrategy (que basicamente define um método abstrato que deve ser implementado por suas subclasses: **traverse_from_source**). As classes que implementam um algoritmo de travessia devem herdar de TraversalStrategy e implementar este algoritmo através do método **traverse_from_source**.

3. **Factory**: este padrão foi utilizado para definir uma interface genérica para o processo de criação de uma instância de TraversalStrategy. Ele recebe uma string que indica qual estratégia deve ser instanciada e retorna esta instância.
