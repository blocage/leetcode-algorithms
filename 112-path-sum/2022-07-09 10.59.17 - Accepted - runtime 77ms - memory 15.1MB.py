class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:return False
        if not(root.left or root.right) and target == root.val:return True
        target -= root.val
        return self.hasPathSum(root.left,target)or self.hasPathSum(root.right,target)