class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind = 0
        while ind < len(strs[0]):
            c = strs[0][ind]
            for i in strs:
                if len(i) <= ind or i[ind] != c: return strs[0][:ind]
            ind += 1
        
        return strs[0][:ind]
        