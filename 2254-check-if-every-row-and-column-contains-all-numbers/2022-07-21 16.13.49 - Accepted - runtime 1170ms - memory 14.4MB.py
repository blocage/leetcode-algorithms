class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        a = [*range(1, len(matrix) + 1)]
        return all(sorted(f)==a for f in matrix) and all(sorted(f)==a for f in zip(*matrix))