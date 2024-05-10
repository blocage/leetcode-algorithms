class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = []
        for i in path.split('/'):
            if i:
                if i == '..':
                    if curr:
                        curr.pop()
                elif i == '.':
                    pass
                else:
                    curr.append(i)
        
        return '/' + '/'.join(curr)