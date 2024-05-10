class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = sorted(nums)
        return nums == l or nums[::-1] == l
        