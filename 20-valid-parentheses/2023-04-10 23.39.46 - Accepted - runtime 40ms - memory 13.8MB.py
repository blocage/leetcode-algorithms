class Solution:
    def isValid(self, s: str) -> bool:
        m = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in m.keys():
                stack.append(i)
            else:
                if not stack or i != m[stack.pop()]:
                    return False
        
        return not stack