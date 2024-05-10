class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        lvl = 0
        while q:
            l = len(q)
            if lvl % 2:
                for i in range(l // 2):
                    a,b = q[i], q[~i]
                    a.val, b.val = b.val, a.val
            for _ in range(l):
                curr = q.popleft()
                if curr.left:
                    q.extend([curr.left, curr.right])
            
            lvl += 1
        
        return root