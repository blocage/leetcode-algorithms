class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in remainders:
                return [remainders[remainder], i]
            remainders[target - remainder] = i