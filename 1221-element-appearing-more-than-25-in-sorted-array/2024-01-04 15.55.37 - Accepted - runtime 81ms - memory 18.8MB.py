class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        return Counter(arr).most_common(1)[0][0]
        