class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heights = [0] * (n + 1)
        best = 0
        for row in matrix:
            for col in range(n):
                heights[col] = heights[col] + 1 if row[col] == '1' else 0
            stack = [-1]
            for col in range(n + 1):
                while heights[col] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = col - stack[-1] - 1
                    best = max(best, h * w)
                stack.append(col)
        return best