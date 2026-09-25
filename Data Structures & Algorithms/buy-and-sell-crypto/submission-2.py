class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        max_profit = 0

        for day in range(len(prices)):
            if prices[day] < prices[buy_day]:
                buy_day = day
            
            max_profit = max(max_profit, prices[day] - prices[buy_day])
        
        return max_profit
