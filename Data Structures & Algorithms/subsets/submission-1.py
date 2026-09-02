class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(len(result)):
                result.append([nums[i]] + result[j])
            result.append([nums[i]])
        result.append([])
        return result