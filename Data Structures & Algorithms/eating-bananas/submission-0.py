class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, high = 1, max(piles)
        history = {}

        while lo <= high:
            mid = (lo + high) // 2

            res = feasible(mid, piles, h)
            history[mid] = res

            if res == 1: 
                high = mid -1
            else:
                lo = mid + 1
        
        if history[mid] == 1:
            return mid
        else:
            return mid + 1



def feasible(num, piles, h):
    counter = 0
    for pile in piles:
        counter += math.ceil(pile/num)
    
    if counter <= h:
        return 1
    else: 
        return -1