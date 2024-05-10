class Solution:        
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.extend(reversed(node.children))
        
        return res