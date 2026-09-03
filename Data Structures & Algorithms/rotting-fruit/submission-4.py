from collections import deque
from typing import List, Set

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # 1. Riempi la coda e conta le arance fresche
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # Se non ci sono arance fresche, il tempo è 0
        if fresh_count == 0:
            return 0

        length = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # 2. Esegui la BFS
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for direction in directions:
                    if not self._feasibleDirection(grid, i, j, direction):
                        continue

                    dr, dc = direction
                    grid[i + dr][j + dc] = 2
                    queue.append((i + dr, j + dc))
                    fresh_count -= 1 # Riduciamo il conteggio delle fresche!

            length += 1
        
        # 3. Se sono rimaste arance fresche che non abbiamo raggiunto
        if fresh_count > 0:
            return -1
            
        return length - 1

    def _feasibleDirection(self, grid: List[List[int]], i: int, j: int, direction: List[int]) -> bool:
        ROWS, COLS = len(grid), len(grid[0])
        dr, dc = direction
        r, c = i + dr, j + dc
        
        if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1:
            return False
        return True