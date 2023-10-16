import heapq
import collections

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
