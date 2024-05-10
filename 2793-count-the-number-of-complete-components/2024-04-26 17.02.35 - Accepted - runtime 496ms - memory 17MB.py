class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        d = [[] for i in range(n)]
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)
        
        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i]: continue
            bfs = [i]
            visited[i] = 1
            for j in bfs:
                for k in d[j]:
                    if not visited[k]:
                        bfs.append(k)
                        visited[k] = 1
            if all(len(d[j]) == len(bfs) - 1 for j in bfs):
                res += 1
        
        return res