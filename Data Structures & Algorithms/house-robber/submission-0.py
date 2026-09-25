class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_in_steps_of_1 = 0
        rob_in_steps_of_2 = 0

        for n in nums: #Calculates for taking the list one at a time. Reducing each element by 1 it takes me to the next smaller subarray short of 1
            temp = max(n+rob_in_steps_of_1, rob_in_steps_of_2)
            rob_in_steps_of_1 = rob_in_steps_of_2
            rob_in_steps_of_2 = temp
        
        return rob_in_steps_of_2
