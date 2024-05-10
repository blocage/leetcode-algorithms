class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        d, clones = deque([node]), {node.val: Node(node.val)}
        while d:
            curr = d.popleft()
            curr_clone = clones[curr.val]
            for i in curr.neighbors:
                if i.val not in clones:
                    clones[i.val] = Node(i.val)
                    d.append(i)
                curr_clone.neighbors.append(clones[i.val])
        
        return clones[node.val]