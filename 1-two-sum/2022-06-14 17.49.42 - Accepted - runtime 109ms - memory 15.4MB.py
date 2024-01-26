class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind, i in enumerate(nums):
            rem = target - i
            if i in d:
                return [ind, d[i]]
            d[rem] = ind