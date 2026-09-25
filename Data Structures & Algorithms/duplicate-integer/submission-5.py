class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storer = set() 
        for n in nums:
            if n in storer:
                return True
            storer.add(n)
        return False