class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        for i in sorted(nums, reverse=True):
            if -i in s:
                return i
        
        return -1