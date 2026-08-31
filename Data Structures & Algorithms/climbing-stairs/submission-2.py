class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2: 
            return 2
        i = n-3
        array = [0] * n
        array[n-1] = 1
        array[n-2] = 2

        while i >= 0:
            array[i] = array[i+1] + array[i+2]
            i -= 1

        return array[0]
        
