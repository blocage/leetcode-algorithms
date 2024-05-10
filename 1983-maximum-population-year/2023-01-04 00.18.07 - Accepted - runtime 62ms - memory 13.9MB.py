class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        best_alive = alive = best_year = 0
        years = []
        logs.sort()
        for a,b in logs:
            if years:
                m = heapq.nsmallest(1, years)[0]
                if a >= m:
                    heapq.heappop(years)
                    alive -= 1
            
            alive += 1
            heapq.heappush(years, b)
            if alive > best_alive:
                best_year = a
                best_alive = alive
        
        
        return best_year