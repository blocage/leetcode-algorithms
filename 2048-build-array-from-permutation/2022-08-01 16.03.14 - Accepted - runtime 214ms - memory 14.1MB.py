class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        for i in range(l):
            res[i] = nums[nums[i]]
        
        return res
        