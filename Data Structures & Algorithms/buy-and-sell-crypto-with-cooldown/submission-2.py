class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} 

        def depth(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # So above we have defined 2 bases cases.
            # Now we need to calculate (i. buying) for cases
            # Case 1: We are buying
            # Case 2: We are selling

            if buying:
                buy_profit = depth(i + 1, False) - prices[i]
                cooldown_profit = depth(i + 1, True)
                dp[(i, buying)] = max(buy_profit, cooldown_profit)
            else:
                sell_profit = depth(i + 2, True) + prices[i]
                cooldown_profit = depth(i + 1, False)
                dp[(i, buying)] = max(sell_profit, cooldown_profit)
            
            return dp[(i, buying)]
        
        return depth(0, True)
