class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        c = 0
        for i in range(2, len(cost)):
            c = cost[i] + min(a, b)
            a, b = b, c
        return min(a,b)