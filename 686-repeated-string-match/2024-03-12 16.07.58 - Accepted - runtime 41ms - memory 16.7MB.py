class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        t = ceil(len(b) / len(a))
        return t * (b in a * t) or (t + 1) * (b in a * (t + 1)) or -1