class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        last = None
        count = 0
        for R in range(len(nums)):
            if nums[R] == last:
                count += 1
                if count <= 1:
                    nums[L] = nums[R]
                    L += 1
                    last = nums[R]
                continue
            else:
                count = 0
                nums[L] = nums[R]
                L += 1
                last = nums[R]
        return L