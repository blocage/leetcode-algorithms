class Solution:
    def partitionString(self, s: str) -> int:
        i, ans, flag = 0, 1, 0
        while i < len(s):
            val = ord(s[i]) - ord('a')
            if flag & (1 << val):
                flag = 0
                ans += 1
            flag |= 1 << val
            i += 1
        return ans