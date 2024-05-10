class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        a = b = r = 0
        l, L = len(g), len(s)
        g.sort()
        s.sort()
        while a < l and b < L:
            print(g[a], s[b])
            if g[a] <= s[b]:
                r += 1
                a += 1
                b += 1
            else:
                b += 1

        return r