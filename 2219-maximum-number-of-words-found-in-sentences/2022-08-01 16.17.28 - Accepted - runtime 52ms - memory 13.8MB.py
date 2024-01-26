class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(f.count(' ')+1 for f in sentences)