class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        a = r = 0
        for i in gain:
            a += i
            r = max(a, r)
        return r