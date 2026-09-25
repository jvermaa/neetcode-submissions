class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        sack = [] # (value, index)

        for i, v in enumerate(temperatures):
            while sack and v > sack[-1][0]:
                result[sack[-1][1]] = i - sack[-1][1]
                sack.pop()
            
            sack.append((v, i))
        
        return result
            