class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = set()
        for i in nums:
            if i in mapper:
                return True
            else:
                mapper.add(i)
        return False