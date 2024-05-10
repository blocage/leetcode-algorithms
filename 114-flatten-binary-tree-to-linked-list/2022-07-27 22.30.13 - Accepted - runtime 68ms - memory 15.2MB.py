class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                p = curr.left
                while p.right:p = p.right
                p.right = curr.right
                curr.right = curr.left
                curr.left = None
            
            curr = curr.right