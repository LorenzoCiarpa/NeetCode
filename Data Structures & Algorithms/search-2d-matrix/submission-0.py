class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m*n) - 1

        while low <= high:
            mid = (low + high) // 2

            i = mid // n
            j = mid - (n*i)

            res = self.isCorrect(matrix[i][j], target)
            if res == 0:
                return True
            
            if res == -1:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

    
    def isCorrect(self, n, target):
        if n == target:
            return 0
        if n > target:
            return -1
        if n < target:
            return 1