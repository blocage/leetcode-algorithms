class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k = sorted(nums)
        return [k.index(f)for f in nums]