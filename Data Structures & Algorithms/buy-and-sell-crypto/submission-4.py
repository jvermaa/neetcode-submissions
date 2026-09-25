class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = prices[0]
        maxProfit = 0
        currentProfit = 0
        for i in range(1, len(prices)):
            r = prices[i]
            if r <= buy_day:
                buy_day = r
                currentProfit = 0
            else:
                currentProfit = r - buy_day

            maxProfit = max(maxProfit, currentProfit)
        
        return maxProfit
