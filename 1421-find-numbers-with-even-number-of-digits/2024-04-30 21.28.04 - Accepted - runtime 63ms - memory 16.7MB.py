class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(f)) % 2 == 0 for f in nums)