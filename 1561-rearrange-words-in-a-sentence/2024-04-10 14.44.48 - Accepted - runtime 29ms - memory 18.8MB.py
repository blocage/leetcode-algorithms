class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(), key=len)).capitalize()