class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for i in map(ord, s):
            dp[i] = max(dp[i - k: i + k + 1]) + 1
        
        return max(dp)