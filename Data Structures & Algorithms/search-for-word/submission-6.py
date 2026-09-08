class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if m == n == len(word) == 1 and board[0][0] == word[0]:
            return True
        for i in range(m):
            for j in range(n):
                visit = set()
                res = self.dfs(board, i, j, 0, word, visit)
                if res:
                    return True
        return False
        
    def dfs(self, board, i, j, curr, word, visit):
        m, n = len(board), len(board[0])
        if curr == len(word):
            return True

        if not self.feasibleDir(i, j, m, n) \
            or (i, j) in visit \
            or board[i][j] != word[curr]:
            return False


        
        visit.add((i, j))
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        for d in directions:
            xi, xj = i + d[0], j + d[1]
            
            
            res = self.dfs(board, xi, xj, curr + 1, word, visit)
            if res:
                return res
        visit.remove((i, j))
        return False
            
        
    def feasibleDir(self, i, j, m, n):
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False