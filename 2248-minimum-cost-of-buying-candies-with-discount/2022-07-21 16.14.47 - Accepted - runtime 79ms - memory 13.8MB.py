class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        heapq._heapify_max(cost)
        res = 0
        for i in range(1, len(cost) + 1):
            if i % 3:res += heapq._heappop_max(cost)
            else:heapq._heappop_max(cost)

        return res