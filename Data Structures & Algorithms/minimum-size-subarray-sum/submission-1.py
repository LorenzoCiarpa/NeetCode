class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        currSum = 0
        L = 0
        
        for R in range(len(nums)):
            currSum += nums[R]

            while currSum >= target:
                length = min(length, R - L + 1)
                currSum -= nums[L]
                L += 1
            
        
        return 0 if length == float("inf") else length
            
                