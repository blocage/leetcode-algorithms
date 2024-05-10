class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = int(str(x)[1:][::-1])
            if num > 2147483648:
                return 0
            return -num
        else:
            num = int(str(x)[::-1])
            if num > 2147483648:
                return 0
            return num