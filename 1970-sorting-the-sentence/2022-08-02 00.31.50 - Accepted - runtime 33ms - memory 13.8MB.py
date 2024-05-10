class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        for i in a[:]:
            a[int(i[-1]) - 1] = i[:-1]
        
        return ' '.join(a)