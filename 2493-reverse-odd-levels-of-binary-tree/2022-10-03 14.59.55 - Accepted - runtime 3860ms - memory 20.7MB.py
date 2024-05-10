class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        level = 0
        while q:
            l = len(q)
            if level % 2:
                for i in range(l // 2):
                    left, right = q[i], q[~i]
                    left.val, right.val = right.val, left.val
            for _ in range(l):
                curr = q.pop(0)
                if curr.left:
                    q += [curr.left, curr.right]
            
            level += 1
                
            
        return root