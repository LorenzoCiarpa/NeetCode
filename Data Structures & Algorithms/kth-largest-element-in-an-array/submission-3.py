

class Solution:
    def initNums(self, nums: List[int]) -> None: 
        nums.insert(0,0)

        curr = (len(nums) - 1) // 2

        # O(n)
        while curr > 0:
            i = curr

            while (i * 2) < len(nums):

                if (i * 2) + 1 < len(nums) and nums[(i * 2) + 1] > nums[(i * 2)] and nums[i] < nums[(i * 2) + 1]:
                    tmp = nums[(i * 2) + 1]
                    nums[(i * 2) + 1] = nums[i]
                    nums[i] = tmp
                    i = (i * 2) + 1
                elif nums[i] < nums[i * 2]:
                    tmp = nums[i * 2]
                    nums[i * 2] = nums[i]
                    nums[i] = tmp
                    i = i * 2
                else:
                    break
            
            curr -= 1


    
    
    def pop(self, nums):
        if len(nums) == 1:
            return -1
        if len(nums) == 2:
            return nums[1]
            
        res = nums[1]
        nums[1] = nums.pop()
        i = 1

        while (i * 2) < len(nums):

            if (i * 2) + 1 < len(nums) and nums[(i * 2) + 1] > nums[(i * 2)] and nums[i] < nums[(i * 2) + 1]:
                tmp = nums[(i * 2) + 1]
                nums[(i * 2) + 1] = nums[i]
                nums[i] = tmp
                i = (i * 2) + 1
            elif nums[i] < nums[i * 2]:
                tmp = nums[i * 2]
                nums[i * 2] = nums[i]
                nums[i] = tmp
                i = i * 2
            else:
                break

        return res

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.initNums(nums)
        for _ in range(k-1):
            self.pop(nums)

        return self.pop(nums)

