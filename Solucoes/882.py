import collections
import heapq

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
