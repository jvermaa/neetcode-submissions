class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_map = set()
        for i in nums:
            if i in set_map:
                return True
            set_map.add(i)
        return False