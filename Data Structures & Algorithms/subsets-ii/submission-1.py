class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        curSet = []
        nums = sorted(nums)
        self.helper(0, nums, curSet, subsets)
        return subsets

    def helper(self, i: int, nums: List[int], curSet: List[int], subsets: List[List[int]]) -> None:
        if i >= len(nums):
            subsets.append(curSet.copy())
            return
        
        curSet.append(nums[i])
        self.helper(i + 1, nums, curSet, subsets)
        curSet.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, curSet, subsets)
        return