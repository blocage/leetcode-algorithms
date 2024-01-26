class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d, w, m = costs
        dp = [0] * 30
        dy = set(days)
        for i in range(1, days[-1] + 1):
            if i not in dy:
                dp[i % 30] = dp[(i - 1) % 30]
            else:
                dp[i % 30] = min(dp[(i - 1) % 30] + d, dp[max(0,(i - 7) % 30)] + w, dp[max(0, (i - 30) % 30)] + m)

        return dp[i % 30]