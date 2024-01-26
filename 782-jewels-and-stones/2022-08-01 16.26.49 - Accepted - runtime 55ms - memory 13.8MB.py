class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(f in jewels for f in stones)