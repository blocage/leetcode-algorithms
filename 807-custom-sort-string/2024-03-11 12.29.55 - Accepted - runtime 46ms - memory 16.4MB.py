class Solution:
    def customSortString(self, order: str, s: str) -> str:
        return ''.join(sorted(s, key=lambda x:order.find(x)))
        