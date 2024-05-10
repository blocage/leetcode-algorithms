class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(f != tuple(sorted(f)) for f in zip(*strs))