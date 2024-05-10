class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in range(k):
            if s[i] in 'aeiou':
                count += 1
        
        res = count
        for end in range(k, len(s)):
            start = end - k # 'abcde'
            if s[start] in 'aeiou':
                count -= 1
            if s[end] in 'aeiou':
                count += 1
            res = max(res, count)
        return res