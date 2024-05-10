class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        return ''.join(a*b for a,b in sorted(s.items(), key=lambda x:-x[1]))