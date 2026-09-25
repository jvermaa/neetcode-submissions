class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to hold frequency: list of elements
        frequency_maps = defaultdict(list)
        count = 1
        nums.sort(reverse=True)  # Sort the list in descending order to simplify processing
        current = nums[0]
        
        # Building the frequency map
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
            else:
                frequency_maps[count].append(current)
                current = nums[i]
                count = 1
        
        # Handle the last element
        frequency_maps[count].append(current)
        
        # Collecting the top k frequent elements
        result = []
        for freq in sorted(frequency_maps.keys(), reverse=True):
            for elem in frequency_maps[freq]:
                result.append(elem)
                if len(result) == k:
                    return result
        
        return result