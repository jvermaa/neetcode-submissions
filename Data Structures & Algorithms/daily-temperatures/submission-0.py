class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        diff = [0]*n
        stroke = []

        for i, v in enumerate(temperatures):
            while stroke and stroke[-1][-1] < v:
                o_i, o_v = stroke.pop()
                diff[o_i] = i - o_i
            
            stroke.append((i,v))
        
        return diff
