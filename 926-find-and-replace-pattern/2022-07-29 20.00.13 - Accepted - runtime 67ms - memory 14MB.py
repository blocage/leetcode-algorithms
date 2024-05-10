class Solution:
    def findAndReplacePattern(self, w: List[str], p: str) -> List[str]:
        return [f for f in w if all(f.index(a)==p.index(b) for a,b in zip(f,p))]