class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        w = []
        l = []
        for a,b in matches:
            w.append(a)
            l.append(b)

        w, l = map(Counter, (w, l))
        return [sorted(w.keys() - l.keys()), sorted([a for a,b in l.items() if b == 1])]