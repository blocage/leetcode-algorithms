class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if not s:
                return True
            if i == s[0]:s = s[1:]
        
        return not s