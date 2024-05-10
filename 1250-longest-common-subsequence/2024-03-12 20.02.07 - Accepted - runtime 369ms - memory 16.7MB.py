class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = map(len, (text1, text2))
        dp = [0] * (n + 1)
        for i in text1:
            a = b = 0
            for j, c in enumerate(text2):
                a, b = dp[j + 1], a
                dp[j + 1] = b + 1 if c == i else max(dp[j], a)
        
        return dp[-1]