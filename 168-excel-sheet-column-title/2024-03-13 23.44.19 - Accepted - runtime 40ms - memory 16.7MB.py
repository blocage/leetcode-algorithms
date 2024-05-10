class Solution:
    def convertToTitle(self, n: int) -> str:
        r = ""
        while n > 0:
            r += chr(ord('A') + (n - 1) % 26)
            n = (n - 1) // 26

        return r[::-1]
        