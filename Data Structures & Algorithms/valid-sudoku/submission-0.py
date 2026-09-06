class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        blocks = [set() for i in range(9)]

        for i in range(len(board)):
            row = set()
            for j in range(len(board[0])):
                elem = board[i][j]
                if elem == ".":
                    continue
                if elem in row:

                    return False
                
                if elem in cols[j]:

                    return False
                
                b_idx = self.getBlock(i, j)
                if elem in blocks[b_idx]:
                    return False
                
                row.add(elem)
                cols[j].add(elem)
                blocks[b_idx].add(elem)
        return True

    
    def getBlock(self, i, j):
        r = i // 3
        c = j // 3
        return 3 * r + c