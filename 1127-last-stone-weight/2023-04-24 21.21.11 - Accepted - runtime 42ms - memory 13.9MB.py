class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-f for f in stones]
        heapq.heapify(h)
        while len(h) > 1:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]