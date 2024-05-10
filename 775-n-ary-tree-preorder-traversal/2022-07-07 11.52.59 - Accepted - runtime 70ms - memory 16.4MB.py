class Solution:
    def dfs(self, root, l):
        if not root:return
        if root:l.append(root.val)
        for child in root.children:
            self.dfs(child,l)
            
        
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        
        return res