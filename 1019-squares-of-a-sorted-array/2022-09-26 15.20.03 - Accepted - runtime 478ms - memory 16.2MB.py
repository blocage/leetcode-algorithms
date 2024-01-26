class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(f ** 2 for f in nums)