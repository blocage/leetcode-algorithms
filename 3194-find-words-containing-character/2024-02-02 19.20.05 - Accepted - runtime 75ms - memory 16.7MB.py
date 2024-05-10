class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [f for f in range(len(words)) if x in words[f]]
