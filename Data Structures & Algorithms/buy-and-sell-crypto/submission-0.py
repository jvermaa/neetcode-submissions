class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for n in prices:
            if n < buy:
                buy = n
            max_profit = max(max_profit, n-buy)

        return max_profit