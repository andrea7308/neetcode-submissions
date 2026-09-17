class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

        for i in range(len(prices)):
            for k in range(i):
                if prices[k] < prices[i]:
                    profit = prices[i] - prices[k]
                    res = max(res, profit)

        return res

        
