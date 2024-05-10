class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(f for f in nums if nums.count(f) == 1)