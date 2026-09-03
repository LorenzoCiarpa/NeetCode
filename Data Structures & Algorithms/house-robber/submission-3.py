class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # self.nums = nums
        # return self.recursiveRob(0, 0)
        
        return self.dpRob(nums)

        
        

    def recursiveRob(self, incumbent, idx) -> int:
        if idx >= len(self.nums):
            
            return incumbent
        
        left = self.recursiveRob(incumbent, idx+1)
        right = self.recursiveRob(incumbent + self.nums[idx], idx+2)

        return max(left, right)

    def dpRob(self, nums):
        taken = [0 for i in nums]
        not_taken = [0 for i in nums]

        not_taken[-1] = 0
        taken[-1] = nums[-1]

        not_taken[-2] = nums[-1]
        taken[-2] = nums[-2]

        for i in range(len(nums) -3, -1, -1):
            not_taken[i] = max(taken[i+1], not_taken[i+1])
            taken[i] = nums[i] + max(taken[i+2], not_taken[i+2])
        
        return max(taken[0], not_taken[0])
