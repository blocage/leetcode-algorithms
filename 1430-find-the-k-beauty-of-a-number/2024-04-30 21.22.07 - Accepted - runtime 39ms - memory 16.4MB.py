class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        t = str(num)
        return sum(num % int(t[f:f + k]) == 0 for f in range(len(t) - k + 1)if int(t[f:f + k]))