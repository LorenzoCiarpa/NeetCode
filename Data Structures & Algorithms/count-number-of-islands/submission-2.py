class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visit:
                    self.aux(grid, i, j, visit)
                    count += 1
        return count
    
    def aux(self, grid, r, c, visit) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit:
            return
        
        visit.add((r, c))
        if grid[r][c] == "0":
            return
        
        
        self.aux(grid, r+1, c, visit)
        self.aux(grid, r-1, c, visit)
        self.aux(grid, r, c+1, visit)
        self.aux(grid, r, c-1, visit)
        
        return
