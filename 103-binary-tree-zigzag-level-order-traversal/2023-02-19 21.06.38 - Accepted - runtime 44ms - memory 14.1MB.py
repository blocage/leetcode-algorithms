class Solution:
    def traverse(self, node: Optional[TreeNode], res: dict[int, List[TreeNode]], depth: int) -> None:
        if node:
            res[depth] = res.get(depth, []) + [node.val]
            if node.left:
                self.traverse(node.left, res, depth + 1)
            if node.right:
                self.traverse(node.right, res, depth + 1)
            
            
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = {}
        self.traverse(root, res, 1)
        return [val if key % 2 else val[::-1] for key, val in res.items()]
