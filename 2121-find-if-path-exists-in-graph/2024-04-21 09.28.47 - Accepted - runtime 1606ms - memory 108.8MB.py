class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> bool:
        l = defaultdict(list)
        for a,b in edges:
            l[a].append(b)
            l[b].append(a)
        stack = [src]
        while stack:
            n = stack.pop()
            if n == dst: return True
            while l[n]:stack.append(l[n].pop())

        
        return False