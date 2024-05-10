class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        t = len(arr)
        l = []
        for i in range(t):
            for j in range(t - 1, 0, -1):
                heapq.heappush(l, (arr[i]/arr[j], arr[i], arr[j]))

        for i in range(k):
            _, a, b = heapq.heappop(l)
    
        return a, b