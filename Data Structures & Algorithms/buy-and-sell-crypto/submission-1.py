class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

        for i in range(len(prices)):
            for k in range(i+1, len(prices)):
                profit = prices[k] - prices[i]
                res = max(res, profit)

        return res

        
