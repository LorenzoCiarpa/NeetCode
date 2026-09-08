class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = [False] * len(nums)
        res[-1] = True
        
        for i in range(len(nums) - 2, -1, -1):
            steps = min(len(nums), i + nums[i] + 1)
            for j in range(i, steps):
                if res[j]:
                    res[i] = True
                    break
        return res[0]
            