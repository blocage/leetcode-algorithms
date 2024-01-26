class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        return [nums.index(t), len(nums) - 1 - nums[::-1].index(t)] if t in nums else [-1, -1]