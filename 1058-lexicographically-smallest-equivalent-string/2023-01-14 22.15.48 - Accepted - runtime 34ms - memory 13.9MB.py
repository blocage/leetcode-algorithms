class Solution:
    def find(self, char: str, d: dict[str, str]) -> str:
        if d[char] != char:
            d[char] = self.find(d[char], d)
        return d[char]

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {f:f for f in string.ascii_lowercase}
        
        for a,b in zip(s1, s2):
            x, y = self.find(a, d), self.find(b, d)
            if x > y:
                d[x] = y
            else:
                d[y] = x
        
        return ''.join(self.find(f, d) for f in baseStr)