class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h, w = len(matrix), len(matrix[0])
        left = [0] * w
        right = [w] * w
        height = [0] * w
        res = 0
        for i in range(h):
            l, r = 0, w
            for j in range(w):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            
            for j in range(w):
                if matrix[i][j] == '1': left[j] = max(left[j], l)
                else: left[j] = 0; l = j + 1
            
            for j in range(w - 1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], r)
                else: right[j] = w; r = j
            
            for j in range(w):
                res = max(res, (right[j]-left[j])*height[j])
        
        return res