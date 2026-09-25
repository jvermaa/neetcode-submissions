class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency_as_index = [[] for n in range(len(nums) + 1)]
        result = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for number, frequency in count.items():
            frequency_as_index[frequency].append(number)
            
        
        for i in range(len(frequency_as_index)-1, 0 , -1):
                for j in frequency_as_index[i]:
                    result.append(j)
                    if len(result) == k:
                        return result