class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        
        grid = [[None for _ in range(n)] for _ in range(m)]
        grid[m-1][n-1] = 1 - obstacleGrid[m-1][n-1]

        for j in range(n-2, -1, -1):
            grid[m-1][j] = min(1 - obstacleGrid[m-1][j], grid[m-1][j+1])



        for i in range(m - 2, -1 ,-1):
            row = [0] * n
            if obstacleGrid[i][-1] == 1:
                row[-1] = 0
            else:
                row[-1] = grid[i+1][-1]

            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j] == 1:
                    row[j] = 0
                else:
                    row[j] = grid[i+1][j] + row[j+1]
            grid[i] = row

        return grid[0][0]