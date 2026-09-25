class Solution:
    def climbStairs(self, n: int) -> int:
        first_step = 1
        second_step = 1

        for i in range(n-1):
            first_step += second_step
            second_step = first_step - second_step
        
        return first_step