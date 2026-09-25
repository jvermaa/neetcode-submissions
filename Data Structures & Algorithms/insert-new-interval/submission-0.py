class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Add new interval and sort by start time
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        # Initialize result array with first interval
        merged = []
        
        for interval in intervals:
            # If merged is empty or no overlap, add current interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # If there is overlap, merge with the last interval in result
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged