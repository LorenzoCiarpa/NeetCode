class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visit:
                    res = self.aux(grid, i, j, visit)
                    if res > best:
                        best = res
        return best
    
    def aux(self, grid, r, c, visit) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit:
            return 0
        
        visit.add((r, c))
        
        if grid[r][c] == 0:
            return 0
        
        count = 0
        count += self.aux(grid, r+1, c, visit)
        count += self.aux(grid, r-1, c, visit)
        count += self.aux(grid, r, c+1, visit)
        count += self.aux(grid, r, c-1, visit)
        count += 1

        return count