class Solution:
    def isValid(self, s: str) -> bool:
        m = {'(': ')', '{': '}', '[': ']'}
        d = {'(': 0, '{': 0, '[': 0}
        o = ''
        for i in s:
            if i in '({[':
                d[i] += 1
                o += i
            else:
                if not o:
                    return False
                if m[o[-1]] != i:
                    return False
                d[o[-1]] -= 1
                if d[o[-1]] < 0:
                    return False
                o = o[:-1]
        
        return all(f == 0 for f in d.values())