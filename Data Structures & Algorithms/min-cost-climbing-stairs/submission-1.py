import copy 

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        dyna = copy.deepcopy(cost)
        dyna.append(0)
        
        for i in range(len(cost)-2, -1, -1):
            dyna[i] = min((dyna[i] + dyna[i+1]), (dyna[i] + dyna[i+2]))

        return min(dyna[0], dyna[1])