class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[None for _ in range(n)] for _ in range(m)]
        grid[-1] = [1 for _ in range(n)]

        for i in range(m - 2, -1 ,-1):
            row = [0] * n
            row[-1] = 1

            for j in range(n-2, -1, -1):
                row [j] = grid[i+1][j] + row[j+1]
            grid[i] = row

        return grid[0][0]