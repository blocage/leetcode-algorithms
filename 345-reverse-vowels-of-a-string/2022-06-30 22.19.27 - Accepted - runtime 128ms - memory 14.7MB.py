class Solution:
    def reverseVowels(self, s: str) -> str:
        a = ''.join(f for f in s[::-1]if f.lower() in 'aeiou')
        f = 0
        res = ''
        for i in s:
            if i.lower()in 'aeiou':res += a[f];f+=1
            else:res += i
        
        return res