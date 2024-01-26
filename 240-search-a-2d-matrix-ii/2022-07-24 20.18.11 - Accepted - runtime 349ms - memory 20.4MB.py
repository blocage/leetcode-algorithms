class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in f for f in matrix)