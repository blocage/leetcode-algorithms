class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        columns, rows = [0] * n, [0] * m
        for r,c in indices:
            rows[r] += 1
            columns[c] += 1
        return sum((r + c) % 2 for c in columns for r in rows)