class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_in_steps_of_1 = 0 # Starting the index from 0
        rob_in_steps_of_2 = 0 # Starting the index from 0

        for n in nums: # I will run a forloop to check for the robbing values of each step. Either the n or n+1 and then get their maxes
            temp = max(n + rob_in_steps_of_1, rob_in_steps_of_2) #comparing bw the newly computed robvalue and previous robmax
            rob_in_steps_of_1 = rob_in_steps_of_2
            rob_in_steps_of_2 = temp
        
        return rob_in_steps_of_2
