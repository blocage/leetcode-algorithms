class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        check = 0
        while(check < len(min(strs,key=len)) and len(set(f[check]for f in strs)) == 1):
            res += strs[0][check]
            check += 1
        
        return res