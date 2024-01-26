class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _len = len(nums)
        for i in range(_len):
            for j in range(i + 1, _len):
                if nums[i] + nums[j] == target: return [i, j]