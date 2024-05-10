# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        curr = deque([root])
        while curr:
            lvl = []
            for i in range(len(curr)):
                n = curr.popleft()
                lvl.append(n.val)
                if n.left:
                    curr.append(n.left)
                if n.right:
                    curr.append(n.right)

            pos = {m:j for j,m in enumerate(sorted(lvl))}
            vis, tot = [0] * len(lvl), 0
            for i in range(len(lvl)):
                cnt = 0
                while not vis[i] and i != pos[lvl[i]]:
                    vis[i], i = 1, pos[lvl[i]]
                    cnt += 1
                tot += max(0, cnt-1) 
            res += tot
        
        return res
