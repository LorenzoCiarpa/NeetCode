class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(len(result)):
                tmp = [nums[i]]
                for elem in result[j]:
                    tmp.append(elem)
                result.append(tmp)
            result.append([nums[i]])
        result.append([])
        return result