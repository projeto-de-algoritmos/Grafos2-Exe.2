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
