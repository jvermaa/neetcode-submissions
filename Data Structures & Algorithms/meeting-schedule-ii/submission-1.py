"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        array_of_start_times = sorted([i.start for i in intervals])
        array_of_end_times = sorted([i.end for i in intervals])

        start_array_pointer = 0
        end_array_pointer = 0
        result, count = 0, 0
        while start_array_pointer < len(intervals):
            if array_of_start_times[start_array_pointer] < array_of_end_times[end_array_pointer]:
                count += 1
                start_array_pointer +=1
            else:
                count -= 1
                end_array_pointer += 1
            result = max(result, count)
        
        return result