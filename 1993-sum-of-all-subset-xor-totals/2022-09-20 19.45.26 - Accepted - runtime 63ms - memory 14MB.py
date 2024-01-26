class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return eval('|'.join(map(str,nums))) * int(pow(2, len(nums)-1))