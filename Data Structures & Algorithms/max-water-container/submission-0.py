class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maxWater = 0

        while L < R:
            incumbent = min(heights[L], heights[R]) * (R - L)
            maxWater = max(maxWater, incumbent)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return maxWater