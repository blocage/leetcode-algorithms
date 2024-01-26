class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop = [0] * 101
        res = 0
        for a,b in logs:
            pop[a - 1950] += 1
            pop[b - 1950] -= 1
        
        for i in range(101):
            pop[i] += pop[i - 1]
            if pop[i] > pop[res]:
                res = i
        
        return res + 1950