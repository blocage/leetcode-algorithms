class Solution:
    def dfs(self, node: Optional[TreeNode], res: list[int]) -> None:
        if node:
            res.append(node.val)
            self.dfs(node.left, res)
            self.dfs(node.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        self.dfs(root, res)
        return res