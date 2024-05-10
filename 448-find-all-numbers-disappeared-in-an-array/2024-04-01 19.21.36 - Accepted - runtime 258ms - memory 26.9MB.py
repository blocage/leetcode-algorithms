class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [f for f in range(1, len(nums) + 1) if f not in s]