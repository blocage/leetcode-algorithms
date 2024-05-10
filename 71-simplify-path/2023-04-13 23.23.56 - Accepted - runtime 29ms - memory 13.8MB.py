class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = []
        for i in path.split('/'):
            if i:
                if i == '.':pass
                elif i == '..':
                    if curr:curr.pop()
                else:curr.append(i)
        
        return '/' + '/'.join(curr)