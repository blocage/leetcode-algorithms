class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        r = 1
        for i in range(1, len(nums)):
            dp[i] = 1 + max([dp[f] for f in range(i)if nums[i] > nums[f]]or [0])
            r = max(r, dp[i])
        
        return r
