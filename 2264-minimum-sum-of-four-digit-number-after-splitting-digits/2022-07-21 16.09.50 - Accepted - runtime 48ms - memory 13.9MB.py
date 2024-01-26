class Solution:
    def minimumSum(self, num: int) -> int:
        a,b,c,d = sorted(str(num))
        return int(a + c) + int(b + d)