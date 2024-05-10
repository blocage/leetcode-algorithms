class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)