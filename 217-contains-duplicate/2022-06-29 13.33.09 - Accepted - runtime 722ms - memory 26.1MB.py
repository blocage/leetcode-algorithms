class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))