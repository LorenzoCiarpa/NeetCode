class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        nums = sorted(nums)
        self.helper(0, nums, 0, [], combos, target)
        return combos

    def helper(self, i,  nums, curSum, curCombo, combos, target):
        if curSum == target:
            combos.append(curCombo.copy())
        
        if i >= len(nums):
            return
        
        curCombo.append(nums[i])
        curSum += nums[i]

        if curSum > target:
            curCombo.pop()
            curSum -= nums[i]
            return

        self.helper(i, nums, curSum, curCombo, combos, target)

        curCombo.pop()
        curSum -= nums[i]

        self.helper(i + 1, nums, curSum, curCombo, combos, target)
        return