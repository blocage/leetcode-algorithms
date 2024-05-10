from re import search
class Solution:
    def myAtoi(self, s: str) -> int:
        m = search(r'^([\-\+]?\d+)', s.strip())
        n = int(m.group(1)) if m else 0
        return min(max(n, -2147483648), 2147483647)
