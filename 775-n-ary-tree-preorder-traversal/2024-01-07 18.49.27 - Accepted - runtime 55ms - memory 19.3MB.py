"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def traverse(self, node):
        yield node.val
        if node.children:
            for n in node.children:
                yield from self.traverse(n)

    def preorder(self, root: 'Node') -> List[int]:
        return list(self.traverse(root)) if root else []