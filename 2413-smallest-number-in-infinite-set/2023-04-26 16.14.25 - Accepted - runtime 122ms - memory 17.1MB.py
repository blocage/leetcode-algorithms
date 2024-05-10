class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.min = 1

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        
        self.min += 1
        return self.min - 1

    def addBack(self, num: int) -> None:
        if self.min > num and num not in self.heap:
            heapq.heappush(self.heap, num)