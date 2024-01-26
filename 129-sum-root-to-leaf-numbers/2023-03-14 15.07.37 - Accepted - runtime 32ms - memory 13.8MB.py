class Solution:
    def get_nums(self, node: Optional[TreeNode], num: str = ''):
        if node:
            num = num + str(node.val)
            if node.left or node.right:
                for sub in (node.left, node.right):
                    if sub:
                        yield from self.get_nums(sub, num)
            else:
                yield num
        else:
            yield num
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum(map(int, self.get_nums(root)))