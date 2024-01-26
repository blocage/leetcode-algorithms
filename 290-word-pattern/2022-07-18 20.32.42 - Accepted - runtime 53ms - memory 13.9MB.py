class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern) == len(s := s.split()) and list(map(pattern.index, pattern)) == list(map(s.index, s))