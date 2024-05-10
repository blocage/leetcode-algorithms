class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        even = True
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if even:
                    if node.val % 2 == 0: return False
                    if prev and prev.val >= node.val: return False
                else:
                    if node.val % 2: return False
                    if prev and prev.val <= node.val: return False
                queue += filter(None, (node.left, node.right))
                prev = node
            even = not even
        return True 