class Solution:
    def climbStairs(self, n: int) -> int:
        
        last = 1
        last_last = 1

        for i in range(n-1):
            temp = last
            last = last + last_last
            last_last = temp
        
        return last