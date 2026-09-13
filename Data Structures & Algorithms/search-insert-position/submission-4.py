class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        mid = (L + R) // 2


        while L < R:

            mid = (L + R) // 2

            if nums[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        
        if nums[mid] == target:
            return mid
        
        if nums[L] < target:
            return L + 1
        else:
            return L
