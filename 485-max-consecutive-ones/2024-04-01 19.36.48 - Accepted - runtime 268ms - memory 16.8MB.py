class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = res = 1
        for i in range(1, len(nums)):
            if nums[i] and nums[i - 1]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
    
        return max(res, cur) if any(nums) else 0