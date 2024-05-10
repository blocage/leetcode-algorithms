from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = Counter(nums).values()
        if min(l) == 1:
            return -1
        return sum(f // 3 + (f % 3 > 0) for f in l)