class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        
        while L < R:
            mid = (L + R) // 2
            # print(f"L: {L}, R: {R}, mid: {mid}")

            if nums[R] > nums[mid]:
                R = mid
            elif nums[L] < nums[mid]:
                L = mid
            else:
                break
        return nums[R]
