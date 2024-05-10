class Solution:
    def countStudents(self, s: List[int], sa: List[int]) -> int:
        c = Counter(s)
        n, k = len(s), 0
        while k < n and c[sa[k]]:
            c[sa[k]] -= 1
            k += 1
        return n - k
        