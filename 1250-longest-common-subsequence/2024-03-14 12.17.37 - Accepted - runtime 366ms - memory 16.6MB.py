class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)
        for i in text1:
            a = b = 0
            for j, c in enumerate(text2):
                a, b = dp[j + 1], a
                dp[j + 1] = 1 + b if i == c else max(dp[j], a)

        return dp[-1]