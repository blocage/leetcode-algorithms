class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        q = deque([('0000', 0)])
        vis = set('0000')
        while q:
            st, cnt = q.popleft()
            if st == target: return cnt
            if st in dead: continue
            for i in range(4):
                n = int(st[i])
                for move in (-1, 1):
                    new_st = f'{st[: i]}{(n + move) % 10}{st[i + 1:]}'
                    if new_st not in vis:
                        vis.add(new_st)
                        q.append((new_st, cnt + 1))

        return -1