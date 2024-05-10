class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(a*b for a,b in sorted(Counter(s).items(), key=lambda x:-x[1]))