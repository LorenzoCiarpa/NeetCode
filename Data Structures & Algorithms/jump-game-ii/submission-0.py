class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [False] * len(nums)
        res[-1] = True

        jumps = [0] * len(nums)
        jumps[-1] = 0
        
        for i in range(len(nums) - 2, -1, -1):
            steps = min(len(nums), i + nums[i] + 1)
            smallest = float("inf")
            for j in range(i, steps):
                if res[j]:
                    res[i] = True
                    smallest = min(smallest, jumps[j])

            jumps[i] = smallest + 1
            
        return jumps[0]
            