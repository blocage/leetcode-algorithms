class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = set(nums)
        res = 1
        while res in n:res += 1
        return res