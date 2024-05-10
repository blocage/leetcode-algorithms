class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return filter(lambda x: x, separator.join(words).split(separator))