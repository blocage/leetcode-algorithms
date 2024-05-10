class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, st = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':st.append(i)
            else:
                if st:
                    p = st.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        
        return max(dp)