class Solution:
    def maxDepth(self, s: str) -> int:
        curr = res = 0
        for i in s:
            if i == '(':
                curr += 1
            elif i == ')':
                res = max(res, curr)
                curr -= 1
        return res