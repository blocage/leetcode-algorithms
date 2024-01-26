class Solution:
    def rob(self, nums: list[int]) -> int:
        res = [0]
        for i in nums:
            res = [max(res), res[0] + i]
        
        return max(res)