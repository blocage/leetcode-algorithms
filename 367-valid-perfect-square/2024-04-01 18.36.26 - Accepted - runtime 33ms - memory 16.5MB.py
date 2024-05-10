class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num ** .5 % 1 == 0