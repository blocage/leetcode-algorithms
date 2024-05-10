class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from copy import deepcopy
        return deepcopy(node)