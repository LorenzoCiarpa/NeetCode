class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cleanCell = None
        counter = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                cleanCell = i if cleanCell is None else cleanCell
            else:
                counter += 1
            
            if cleanCell is not None and nums[i] != val:
                nums[cleanCell] = nums[i]
                cleanCell += 1

        return counter