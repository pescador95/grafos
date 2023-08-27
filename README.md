# grafos
Alguns exemplos de grafos.


# Grafos não Ponderados

# Busca em Largura (BFS - Breadth-First Search):
A busca em largura explora os nós vizinhos antes de explorar os nós mais distantes. Ela usa uma fila para manter os nós a serem visitados.

# Busca em Profundidade (DFS - Depth-First Search):
A busca em profundidade explora o máximo possível por um ramo antes de retroceder. Pode usar recursão ou uma pilha.

# Busca Exaustiva:
A busca exaustiva explora todas as possíveis soluções. Pode ser usada quando a solução ótima é necessária, mas pode ser lenta para problemas complexos.

# Busca Gulosa (Greedy Search):
A busca gulosa escolhe o próximo nó que parece mais promissor com base em uma heurística. Pode não levar à solução ótima, mas é rápida e eficiente.

# Busca A:*
A busca A* combina a busca em largura com uma função heurística para avaliar a promessa de um nó. É eficiente e garante uma solução ótima se a heurística for admissível.

# Busca em Profundidade Limitada (DLS - Depth-Limited Search):
A busca em profundidade limitada é uma variante da busca em profundidade que define um limite máximo para a profundidade de exploração.

# Busca Iterativa Profunda (IDS - Iterative Deepening Search):
A busca iterativa profunda é uma combinação da busca em profundidade limitada, onde o limite de profundidade aumenta gradualmente.


# Grafos Ponderados 

# Grafo Direcionado Ponderado:
 Nesse tipo de grafo, cada aresta tem um peso associado e tem direção (uma aresta de A para B não é a mesma que uma aresta de B para A).

# Grafo Não Direcionado Ponderado:
 Semelhante ao grafo direcionado ponderado, mas as arestas não têm direção (a aresta entre A e B é a mesma que a aresta entre B e A).

# Árvore de Custo Mínimo (Minimum Spanning Tree):
 Um subgrafo conectado de um grafo ponderado, que abrange todos os vértices, com o mínimo custo total possível.

# Grafo de Fluxo de Rede (Network Flow Graph):
 Um grafo ponderado usado para representar o fluxo de recursos (como tráfego em redes de comunicação) entre os vértices.

# Grafo de Distância Ponderada:
 Cada aresta representa uma distância entre dois vértices. É comum em problemas envolvendo rotas ou sistemas de localização.

# Grafo de Tempo Ponderado:
 Cada aresta representa um intervalo de tempo necessário para viajar entre os vértices. É usado em problemas de planejamento de horários e cronogramas.

# Grafo de Probabilidade Ponderada:
 Cada aresta tem uma probabilidade associada. É usado para representar incertezas em redes, como redes Bayesianas.

# Grafo de Similaridade Ponderada:
 Usado em problemas de análise de dados, onde as arestas representam a similaridade entre os vértices.