class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution = []
        visit = set()
        for L in range(len(nums)):
            dic = {}
            if L > 0 and nums[L] == nums[L-1]:
                continue

            for R in range(len(nums)-1, L, -1):
                if nums[R] in dic and len(dic[nums[R]]) == 2:
                    dic[nums[R]].append(nums[R])
                    if tuple(dic[nums[R]]) in visit: 
                        continue
                    solution.append(dic[nums[R]])
                    visit.add(tuple(dic[nums[R]]))
                    continue

                target = 0 - (nums[R] + nums[L])
                
                if target < nums[L] or target > nums[R]:
                    continue
                
                dic[target] = [nums[L], nums[R]]
        return solution
                
                
                