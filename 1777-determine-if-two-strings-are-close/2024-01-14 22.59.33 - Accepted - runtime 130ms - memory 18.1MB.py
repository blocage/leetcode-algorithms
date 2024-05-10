class Solution:
    def closeStrings(self, a: str, b: str) -> bool:
        A, B = map(Counter, (a, b))
        return sorted(A.values()) == sorted(B.values()) and A.keys() == B.keys()