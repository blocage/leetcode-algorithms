class Solution:
    def closeStrings(self, a: str, b: str) -> bool:
        A, B = map(lambda x: sorted(Counter(x).values()), (a, b))
        return A == B and set(a) == set(b)