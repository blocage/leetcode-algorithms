class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])