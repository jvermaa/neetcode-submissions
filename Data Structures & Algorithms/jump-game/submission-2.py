class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reach represents the furthest index we can reach
        max_reach = 0
        
        # We only need to check up to the second-to-last element
        # because if we can reach the last element, we're done
        for i in range(len(nums)):
            # If we cannot reach the current position, return False
            if i > max_reach:
                return False
                
            # Update max_reach if the current position allows us to jump further
            max_reach = max(max_reach, i + nums[i])
            
            # If we can already reach the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return True