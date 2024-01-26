class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        l = [[0] * m for f in range(n)]
        for r, c in indices:
            for i in l:i[r] += 1
            l[c] = [f+1 for f in l[c]]
        
        return sum(sum(i%2 for i in f)for f in l)
                