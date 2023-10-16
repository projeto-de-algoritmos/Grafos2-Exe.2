# Grafos 2

## Exercícios 2

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Dijkstra, Prim, Kruskal<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0089601  |João Lucas|

## Sobre
O objetivo foi realizar 3 exercícios do juiz online [LeetCode](https://leetcode.com/), com os 3 sendo exercicios considerados dificeis pela plataforma. Os exercicios foram 
* [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)
* [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/).
* [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) 

## Video
O video de apresentação do repositorio foi gravado e postado dentro do repositório.

[Video](/Video/video.mp4)

## Screenshots

### [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)
![Alt text](/images/image.png)
### [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/).
![Alt text](/images/image-1.png)
### [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/) 
![Alt text](/images/image-2.png)

## Instalação
**Linguagem**: [Pyhton](https://www.python.org/)<br>

## Códigos e Soluções

### [Reachable Nodes In Subdivided Graph](/Solucoes/882.py)

~~~Python
class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        # Cria um dicionário de dicionários para armazenar as arestas e seus comprimentos
        e = collections.defaultdict(dict)
        for i, j, l in edges: 
            e[i][j] = e[j][i] = l

        # Cria uma fila de prioridade com o número máximo de movimentos e o nó inicial (0)
        pq = [(-maxMoves, 0)]
        
        # Dicionário para armazenar os nós visitados e o número de movimentos restantes
        seen = {}
        
        # Enquanto a fila de prioridade não estiver vazia
        while pq:
            # Remove o nó com o maior número de movimentos restantes
            moves, i = heapq.heappop(pq)
            
            # Se o nó não foi visitado antes
            if i not in seen:
                # Adiciona o nó ao dicionário seen com o número de movimentos restantes
                seen[i] = -moves
                
                # Para cada nó adjacente
                for j in e[i]:
                    # Calcula o número de movimentos restantes após mover para o nó adjacente
                    moves2 = -moves - e[i][j] - 1
                    
                    # Se o nó adjacente não foi visitado antes e ainda há movimentos restantes
                    if j not in seen and moves2 >= 0:
                        # Adiciona o nó adjacente à fila de prioridade
                        heapq.heappush(pq, (-moves2, j))
        
        # Inicializa o resultado com o número de nós visitados
        res = len(seen)
        
        # Para cada aresta
        for i, j, k in edges:
            # Adiciona ao resultado o mínimo entre a soma dos movimentos restantes nos nós i e j e o comprimento da aresta
            res += min(seen.get(i, 0) + seen.get(j, 0), e[i][j])
        
        return res
~~~

Este código é uma implementação do algoritmo de Dijkstra para encontrar todos os nós alcançáveis em um gráfico. Ele começa do nó 0 e usa uma fila de prioridade para sempre escolher o nó com o maior número de movimentos restantes. Ele verifica todos os nós adjacentes a um nó visitado e os adiciona à fila de prioridade se eles não foram visitados antes e ainda há movimentos restantes após mover para eles. O resultado é a soma dos movimentos restantes em todos os nós visitados e a soma dos comprimentos das arestas que podem ser totalmente percorridas.

### [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](/Solucoes/1489.py)

~~~Python
class UnionFind:
    def __init__ (self, n):
        self.parents = list(range(n))
        self.weight = 0
        self.edgeCount = 0

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y, w):
        root1 = self.find(x)
        root2 = self.find(y)

        if root1 != root2:
            self.parents[root2] = root1
            self.weight += w
            self.edgeCount += 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        # Adiciona o índice da aresta como quarto elemento
        edges = [(w,a,b,i) for i, (a,b,w) in enumerate(edges)]
        # Ordena as arestas pelo peso
        edges.sort()

        # Cria um objeto UnionFind e adiciona todas as arestas
        uf1 = UnionFind(n)
        for w, a, b, _ in edges:
            uf1.union(a, b, w)

        # Armazena o peso total mínimo
        minWeight = uf1.weight

        # Listas para armazenar as arestas críticas e pseudo-críticas
        ce = []
        pce = []
        
        m = len(edges)

        # Para cada aresta
        for i in range(m):
            # Cria um novo objeto UnionFind e adiciona todas as arestas exceto a atual
            uf2 = UnionFind(n)
            for j in range(m):
                if i == j:
                    continue
                w,a,b,_ = edges[j]
                uf2.union(a,b,w)
            
            # Se o peso total é maior que o mínimo ou se nem todos os nós estão conectados
            if uf2.weight > minWeight or uf2.edgeCount < n-1:
                # A aresta atual é crítica
                ce.append(edges[i][3])

            else:
                # Cria um novo objeto UnionFind e adiciona a aresta atual e todas as outras arestas
                uf3 = UnionFind(n)
                w,a,b,_ = edges[i]
                uf3.union(a,b,w)
                for j in range(m):
                    w,a,b,_ = edges[j]
                    uf3.union(a,b,w)
                
                # Se o peso total é igual ao mínimo
                if uf3.weight == minWeight:
                    # A aresta atual é pseudo-crítica
                    pce.append(edges[i][3])
                    
        return ce, pce
~~~

Este código é uma implementação do algoritmo de Kruskal para encontrar a árvore geradora mínima em um gráfico. Ele usa a estrutura de dados Union-Find para manter o controle das componentes conectadas. Ele primeiro ordena todas as arestas pelo peso e as adiciona à árvore geradora mínima. Em seguida, para cada aresta, ele verifica se removê-la resultará em um peso total maior ou em um gráfico desconectado. Se sim, a aresta é crítica. Se não, ele verifica se adicionar a aresta à árvore geradora mínima sem essa aresta resultará no mesmo peso total. Se sim, a aresta é pseudo-crítica.

### [Min Cost to Connect All Points](/Solucoes/1584.py)

~~~Python
class Solution(object):
    def minCostConnectPoints(self, points):
        # Função auxiliar para calcular a distância de Manhattan entre dois pontos
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        # Inicialização de variáveis
        n = len(points)  # Número de pontos
        c = collections.defaultdict(list)  # Dicionário para armazenar as distâncias entre os pontos

        # Calcular todas as distâncias entre os pontos e armazená-las no dicionário
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))

        # Inicialização de variáveis para o algoritmo de Prim
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)

        # Algoritmo de Prim para encontrar a árvore geradora mínima
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        

        return ans  # Retornar o custo mínimo para conectar todos os pontos
~~~

Este código implementa o algoritmo de Prim para encontrar a árvore geradora mínima em um grafo completo. A ideia é começar com um ponto arbitrário (neste caso, o ponto 0), e então iterativamente adicionar o ponto mais próximo (ou seja, a aresta de menor peso) ao conjunto de pontos já visitados até que todos os pontos tenham sido visitados. A soma das distâncias (ou pesos das arestas) na árvore geradora mínima é o custo mínimo para conectar todos os pontos. A distância entre dois pontos é calculada usando a distância de Manhattan.

