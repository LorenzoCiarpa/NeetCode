class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        adj = {}
        for elem in nums:
            adj[elem] = []
        
        for elem in nums:
            if elem + 1 in adj:
                adj[elem].append(elem + 1)
            if elem - 1 in adj: 
                adj[elem].append(elem - 1)

        longest = 0

        queue = deque()
        visit = set()
        for n in nums:
            if n in visit:
                continue
            queue.append(n)

            counter = 0
            while queue:
                node = queue.popleft()
                if node in visit:
                    continue

                counter += 1
                visit.add(node)

                for neigh in adj[node]:
                    queue.append(neigh)
                
            
            longest = max(longest, counter)


        return longest

        
        
        
    
    """
    This version handles the following case:
    Given an array, the consecutive suqence must be a sub sequence
    of the array itself, meaning that i can consider numbers greater than 1 of element
    i-th only looking forward and not also backward.
    Ex: nums = [0,3,2,5,4,6,1,1] -> Result 2
    Because the possibile consecutive subsequences are [3, 4] or [0, 1]
    """

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     longest = 0
    #     hashMap = {}

    #     for i, elem in enumerate(nums):
    #         if elem not in hashMap:
    #             hashMap[elem] = 1

    #         #Handle the case elem already in hashMap
    #         if elem - 1 in hashMap:
    #             hashMap[elem] = hashMap[elem - 1] + 1
            
    #         longest = max(longest, hashMap[elem])
            
    #     return longest