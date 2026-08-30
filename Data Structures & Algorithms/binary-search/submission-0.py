class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            res = self.isCorrect(nums[mid], target)
            if not res:
                return mid
            
            if res == -1:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
    
    def isCorrect(self, n: int, target: int) -> int:
        if n == target:
            return 0
        if n > target:
            return 1
        if n < target:
            return -1