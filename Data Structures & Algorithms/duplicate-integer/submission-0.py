class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        history = {}

        for elem in nums:
            if elem not in history:
                history[elem] = 1
            else:
                return True
        return False