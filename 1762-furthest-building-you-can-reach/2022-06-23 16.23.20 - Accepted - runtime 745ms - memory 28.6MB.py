class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, climbed = len(heights), []
        
        for i in range(n - 1):
            if (climb := heights[i + 1] - heights[i]) <= 0:
                continue
            
            heapq.heappush(climbed, climb)
            
            if len(climbed) > ladders:
                bricks -= heapq.heappop(climbed)
            
            if bricks < 0:
                return i
                
        return n - 1