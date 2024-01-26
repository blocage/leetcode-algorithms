class Solution:
    def minimumMoves(self, s: str) -> int:
        r = i = 0
        l = len(s)
        while i < l:
            if s[i] == 'X':
                r += 1
                i += 3
            else:
                i += 1
        return r