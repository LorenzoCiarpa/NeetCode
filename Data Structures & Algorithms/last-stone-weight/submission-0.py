from typing import List

class Solution:

    def push(self, stones, val):
        stones.append(val)
        i = len(stones) - 1

        while i > 1 and stones[i] > stones[i//2]:
            tmp = stones[i]
            stones[i] = stones[i//2]
            stones[i//2] = tmp
            i = i // 2 

        return
    
    def pop(self, stones):
        if len(stones) == 1:
            return -1
        if len(stones) == 2:
            return stones.pop()

        res = stones[1]
        stones[1] = stones.pop()
        i = 1

        while (i * 2) < len(stones):

            if (i * 2) + 1 < len(stones) and stones[(i * 2) + 1] > stones[(i * 2)] and stones[i] < stones[(i * 2) + 1]:
                tmp = stones[(i * 2) + 1]
                stones[(i * 2) + 1] = stones[i]
                stones[i] = tmp
                i = (i * 2) + 1
            elif stones[i] < stones[i * 2]:
                tmp = stones[i * 2]
                stones[i * 2] = stones[i]
                stones[i] = tmp
                i = i * 2
            else:
                break

        return res

    def initStones(self, stones): 
        stones.insert(0,0)

        curr = (len(stones) - 1) // 2

        # O(n)
        while curr > 0:
            i = curr

            while (i * 2) < len(stones):

                if (i * 2) + 1 < len(stones) and stones[(i * 2) + 1] > stones[(i * 2)] and stones[i] < stones[(i * 2) + 1]:
                    tmp = stones[(i * 2) + 1]
                    stones[(i * 2) + 1] = stones[i]
                    stones[i] = tmp
                    i = (i * 2) + 1
                elif stones[i] < stones[i * 2]:
                    tmp = stones[i * 2]
                    stones[i * 2] = stones[i]
                    stones[i] = tmp
                    i = i * 2
                else:
                    break
            
            curr -= 1

    def lastStoneWeight(self, stones: List[int]) -> int:
        # print(f"pre init: {stones}")
        self.initStones(stones)
        print(f"post init: {stones}")
        while len(stones) > 2:
            stone1 = self.pop(stones)
            print(f"post pop1: {stones}")

            stone2 = self.pop(stones)
            print(f"post pop2: {stones}")

            diff = stone1 - stone2

            if diff > 0:
                self.push(stones, diff)
            print(f"post push: {stones}")

            

        if len(stones) == 1:
            return 0
        return stones[1]
        

