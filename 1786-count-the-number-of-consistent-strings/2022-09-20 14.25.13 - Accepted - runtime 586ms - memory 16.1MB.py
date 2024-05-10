class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(f in allowed for f in word) for word in words)