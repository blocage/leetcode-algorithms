class Solution:
    def check(self, root: Optional[TreeNode], res, target) -> bool:
        if not root.left and not root.right:
            yield res + root.val == target
        if root.left:
            if root.right:
                yield from self.check(root.left, res + root.val, target) or self.check(root.right, res + root.val, target)
            yield from self.check(root.left, res + root.val, target)
                
        if root.right:
            yield from self.check(root.right, res + root.val, target)
            
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        return any(self.check(root, 0, targetSum))