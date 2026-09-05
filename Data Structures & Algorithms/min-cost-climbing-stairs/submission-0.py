class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        spend = [0] * len(cost)
        spend[-1] = cost[-1]
        spend[-2] = cost[-2]

        totalCost = 0
        for i in range(len(cost) - 3, -1, -1):
            spend[i] = cost[i] + min(spend[i+1], spend[i+2])
        
        return min(spend[0], spend[1])