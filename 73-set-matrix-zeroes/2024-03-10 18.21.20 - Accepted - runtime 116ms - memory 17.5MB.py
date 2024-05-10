from copy import deepcopy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        mmatrix = deepcopy(matrix)
        for y in range(h):
            for x in range(w):
                if mmatrix[y][x] == 0:
                    for i in range(h):matrix[i][x] = 0
                    for i in range(w):matrix[y][i] = 0

