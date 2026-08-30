class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_numbers = 0
        for elem in nums:
            if elem == 0:
                counter = 0
                continue
            
            else:
                counter += 1
            
            if counter >= max_numbers:
                max_numbers = counter
        
        return max_numbers