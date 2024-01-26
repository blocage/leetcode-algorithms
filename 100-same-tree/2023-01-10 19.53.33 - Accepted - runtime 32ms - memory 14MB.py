class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        
        p_stack = [p]
        q_stack = [q]

        while p_stack or q_stack:
            p = p_stack.pop()
            q = q_stack.pop()
            if p and q:
                if p.val != q.val:
                    return False
                p_stack.extend([p.left, p.right])
                q_stack.extend([q.left, q.right])
            
            else:
                if p != q:return False
        
        return True