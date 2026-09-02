class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {elem: i for i, elem in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in history and i != history[diff]:
                return [i, history[diff]]
        
