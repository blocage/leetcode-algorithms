class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a, b = map(collections.Counter, (s, t))
        return sum((a - b).values())