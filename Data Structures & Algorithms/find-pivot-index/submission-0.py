class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftPrefix, rightPrefix = [0], [0]
        
        total = 0
        for i in range(len(nums) - 1):
            total += nums[i]
            leftPrefix.append(total)
        
        total = 0
        for i in range(len(nums) - 1, 0, -1):
            total += nums[i]
            rightPrefix.append(total)

        rightPrefix = list(reversed(rightPrefix))

        
        for i in range(len(leftPrefix)):
            if leftPrefix[i] == rightPrefix[i]:
                return i
        
        return -1