class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0, 1, 1]
        for i in range(35):
            l.append(sum(l[-3:]))
        
        return l[n]