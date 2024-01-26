class Solution:
    def hammingWeight(self, n: int) -> int:
        return f'{n:b}'.count('1')