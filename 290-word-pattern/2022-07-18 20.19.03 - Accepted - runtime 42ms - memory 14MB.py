class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        D = {}
        B = s.split()
        if len(pattern) != len(B):return False
        for a,b in zip(pattern, B):
            if a in D:
                if D[a] != b:return False
            else:D[a] = b
        return len(D.values()) == len(set(D.values()))