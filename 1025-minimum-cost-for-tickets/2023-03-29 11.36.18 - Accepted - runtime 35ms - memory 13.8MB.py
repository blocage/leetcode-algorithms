class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d, w, m = costs
        costs = [0] * (days[-1] + 1)
        dy = set(days)
        for i in range(1, days[-1] + 1):
            if i not in dy:
                costs[i] = costs[i - 1]
            else:
                costs[i] = min(costs[i - 1] + d, costs[max(0,i - 7)] + w, costs[max(0, i - 30)] + m)

        return costs[-1]