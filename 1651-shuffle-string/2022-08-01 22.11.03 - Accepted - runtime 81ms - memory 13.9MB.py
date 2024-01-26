class Solution:
    def restoreString(self, s: str, d: List[int]) -> str:
        *a, = s
        for i in range(len(s)):
            a[d[i]] = s[i]
        
        return ''.join(a)