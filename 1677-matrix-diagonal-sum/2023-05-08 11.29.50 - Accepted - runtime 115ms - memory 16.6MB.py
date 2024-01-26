class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        s = 0
        for i in range(l):
            s += mat[i][i] + mat[i][~i]
            if l % 2 and l // 2 == i:
                s -= mat[i][i]
            
        return s