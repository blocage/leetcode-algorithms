class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[r], nums[i] = nums[i], nums[r]
                r += 1