class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [f for f in range(left, right + 1)if '0'not in str(f) and all(f%int(i) == 0 for i in str(f))]