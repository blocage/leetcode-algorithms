class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a, b = Counter(), Counter()
        for i in range(len(s)):
            if a[s[i]] != b[t[i]]:
                return False
            a[s[i]] = i + 1
            b[t[i]] = i + 1
        
        return True
