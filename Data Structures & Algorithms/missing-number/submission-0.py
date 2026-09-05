class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = sum(nums)
        n = len(nums)
        theory = (n * (n+1)) // 2
        return theory - result