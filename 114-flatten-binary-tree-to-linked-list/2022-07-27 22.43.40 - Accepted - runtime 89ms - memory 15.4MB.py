class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        while root:
            if root.left:
                right_most = root.left
                while right_most.right:
                    right_most = right_most.right
                right_most.right = root.right
                root.right = root.left
                root.left = None
            
            root = root.right