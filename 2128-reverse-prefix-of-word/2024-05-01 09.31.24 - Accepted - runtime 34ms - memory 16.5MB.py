class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        t = word.find(ch)
        return word[:t + 1][::-1] + word[t + 1:]