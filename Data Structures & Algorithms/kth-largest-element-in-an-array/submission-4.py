class Solution:
    def initNums(self, nums: List[int]) -> None: 
        curr = (len(nums) // 2) - 1

        while curr >= 0:
            i = curr

            while (i * 2) + 1 < len(nums):

                if (i * 2) + 2 < len(nums) and nums[(i * 2) + 2] > nums[(i * 2) + 1] and nums[i] < nums[(i * 2) + 2]:
                    tmp = nums[(i * 2) + 2]
                    nums[(i * 2) + 2] = nums[i]
                    nums[i] = tmp
                    i = (i * 2) + 2
                elif nums[i] < nums[(i * 2) + 1]:
                    tmp = nums[(i * 2) + 1]
                    nums[(i * 2) + 1] = nums[i]
                    nums[i] = tmp
                    i = (i * 2) + 1
                else:
                    break
            
            curr -= 1


    
    
    def pop(self, nums):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
            
        res = nums[0]
        nums[0] = nums.pop()
        i = 0

        while (i * 2) + 1 < len(nums):

            if (i * 2) + 2 < len(nums) and nums[(i * 2) + 2] > nums[(i * 2) + 1] and nums[i] < nums[(i * 2) + 2]:
                tmp = nums[(i * 2) + 2]
                nums[(i * 2) + 2] = nums[i]
                nums[i] = tmp
                i = (i * 2) + 2
            elif nums[i] < nums[(i * 2) + 1]:
                tmp = nums[(i * 2) + 1]
                nums[(i * 2) + 1] = nums[i]
                nums[i] = tmp
                i = (i * 2) + 1
            else:
                break

        return res

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.initNums(nums)
        for _ in range(k-1):
            self.pop(nums)

        return self.pop(nums)