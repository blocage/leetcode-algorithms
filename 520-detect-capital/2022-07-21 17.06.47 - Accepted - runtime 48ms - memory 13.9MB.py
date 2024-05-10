class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.istitle() or word.islower()