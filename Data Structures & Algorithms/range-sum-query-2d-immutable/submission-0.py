class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixes = []
        self.m, self.n = len(matrix), len(matrix[0])

        for i in range(self.m):
            arr = []
            total = 0

            for j in range(self.n):
                total += matrix[i][j]
                arr.append(total)
            self.prefixes.append(arr)

                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            
            arr = self.prefixes[i]
            rightPref = arr[col2]
            leftPref = arr[col1 - 1] if col1 > 0 else 0

            total += (rightPref - leftPref)

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)