class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cum_dump = {}
        for i in range(len(numbers)):
            if target - numbers[i] in cum_dump:
                return [cum_dump[target - numbers[i]] + 1, i+1]
            cum_dump[numbers[i]] = i
    