class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind = 0
        m = len(min(strs, key=len))
        while ind < m:
            c = strs[0][ind]
            for i in strs:
                if i[ind] != c: return strs[0][:ind]
            ind += 1
        
        return strs[0][:ind]
        