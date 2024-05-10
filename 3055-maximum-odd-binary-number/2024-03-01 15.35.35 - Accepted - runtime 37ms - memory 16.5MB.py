class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o = s.count("1")
        z = len(s) - o

        return "1" * (o - 1) + "0" * z + "1"