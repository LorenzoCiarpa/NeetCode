class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        last = None
        for R in range(len(nums)):
            if nums[R] == last:
                continue
            else:
                nums[L] = nums[R]
                L += 1
                last = nums[R]
        return L

