class Solution:
    def invert(self, node: TreeNode) -> TreeNode:
        node.left, node.right = node.right, node.left
        for node in (node.left, node.right):
            if node:self.invert(node)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        self.invert(root)
        
        return root