class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return any(s[f:] + s[:f] == goal for f in range(len(s)))