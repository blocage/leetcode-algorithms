class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return ' '.join(f[f[0] not in 'aeiouAEIOU':] + f[:f[0] not in 'aeiouAEIOU'] + 'ma' + 'a' * ind for ind, f in enumerate(sentence.split(), 1))