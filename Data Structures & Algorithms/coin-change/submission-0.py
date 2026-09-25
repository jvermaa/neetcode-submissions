class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        storer = [float('inf')] * (amount + 1)
        storer[0] = 0

        for i in range(1, len(storer)):
            for c in coins:
                if i - c >= 0:
                    storer[i] = min(storer[i], 1 + storer[i - c])
        
        return storer[amount] if storer[amount] < float('inf') else -1