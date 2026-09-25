class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_of_frequency = {} #Key: number of the list, Val: Freq

        # When I increase the freq of a number in dict_of_freq
        # I pop that number from reverse_dict and move to the next freq
        # Finally, we find the nums from 

        for n in nums:
            dict_of_frequency[n] = dict_of_frequency.get(n, 0) + 1
        
        # A bucket is basically a list of freqs. Index is the freq.
        # so if I have n identical numbers in a list of nums
        # Then it will be stored in the nth index
        # so we need to initialize the bucket to n+1 so its last
        # index is n
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in dict_of_frequency.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(nums), -1, -1):
            result += bucket[i]

            if len(result) == k:
                return result
