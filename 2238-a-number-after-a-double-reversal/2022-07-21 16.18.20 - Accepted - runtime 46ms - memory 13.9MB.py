class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = int(str(num)[::-1])
        return str(a)[::-1] == str(num)