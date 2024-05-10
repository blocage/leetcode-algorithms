class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, suf, pre = [1] * len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre
            pre *= nums[i]
            ans[~i] *= suf
            suf *= nums[~i]
        
        return ans