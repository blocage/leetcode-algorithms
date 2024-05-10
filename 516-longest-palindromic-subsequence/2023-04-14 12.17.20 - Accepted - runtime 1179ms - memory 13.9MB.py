class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(1, n):
            pre = dp[i]
            for j in range(i - 1, -1, -1):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = 2 + pre if j + 1 <= i - 1 else 2
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                pre = temp
        
        return dp[0]

# n = len(s)
#         dp = [1] * n
#         for j in xrange(1, len(s)):
#             pre = dp[j]
#             for i in reversed(xrange(0, j)):
#                 tmp = dp[i]
#                 if s[i] == s[j]:
#                     dp[i] = 2 + pre if i + 1 <= j - 1 else 2
#                 else:
#                     dp[i] = max(dp[i + 1], dp[i])
#                 pre = tmp
#         return dp[0]