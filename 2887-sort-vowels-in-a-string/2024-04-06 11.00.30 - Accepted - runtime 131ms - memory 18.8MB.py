class Solution:
    def sortVowels(self, s: str) -> str:
        r = ''
        l = sorted(f for f in s if f in 'aeiouAEIOU')
        v = 0
        for i in s:
            if i in 'aeiouAEIOU':
                r += l[v]
                v += 1
            else:
                r += i
        
        return r