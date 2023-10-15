import collections

class Solution(object):
    def minCost(self, grid):
        # Obtenha o número de linhas e colunas da grade
        m, n = len(grid), len(grid[0])
        
        # Defina as direções das setas
        arrow = [(0,1), (0,-1), (1,0), (-1,0)]            
        
        # Inicialize uma fila de deque com a posição inicial e o custo inicial
        dp = collections.deque([(0, 0, 0)])
        
        # Inicialize um dicionário para armazenar os custos para cada posição
        costs = {}
        
        # Enquanto a fila não estiver vazia
        while dp:
            # Obtenha a próxima posição e custo da fila
            nx, ny, cost = dp.popleft()
            
            # Enquanto a posição atual estiver dentro da grade e ainda não tiver sido visitada
            while 0 <= nx < m and 0 <= ny < n and (nx, ny) not in costs:
                # Atualize o custo para a posição atual
                costs[nx, ny] = cost
                
                # Adicione todas as posições adjacentes à fila com um custo adicional de 1
                dp += [(nx+dx, ny+dy, cost+1) for dx, dy in arrow]
                
                # Obtenha a direção da seta para a posição atual
                dx, dy = arrow[grid[nx][ny]-1]
                
                # Mova para a próxima posição na direção da seta
                nx, ny = nx+dx, ny+dy
                        
        return costs[m-1,n-1]
