class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = [0] * len(prices)
        tmp [-1] = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            if prices[i] < prices[i+1] or prices[i] < tmp[i+1]:
                tmp[i] = tmp[i+1]
            else:
                tmp[i] = prices[i]
        
        bestProfit = 0
        for i in range(len(prices)):
            bestProfit = max(bestProfit, tmp[i] - prices[i])

        return bestProfit

    

    # def maxProfit(self, prices: List[int]) -> int:
    #     L = 0
    #     profit = 0
    #     for R in range(1, len(prices)):
    #         if prices[R] < prices[R-1]:
    #             profit += prices[R-1] - prices[L] 
    #             L = R
    #     if L < len(prices) - 1:
    #         profit += prices[-1] - prices[L] 
    #     return profit