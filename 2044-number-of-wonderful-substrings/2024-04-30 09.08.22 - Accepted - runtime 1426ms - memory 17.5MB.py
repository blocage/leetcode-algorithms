class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1024
        res = cur = 0
        for i in word:
            cur ^= 1 << (ord(i) - 97)
            res += count[cur]
            res += sum(count[cur ^ (1 << f)] for f in range(10))
            count[cur] += 1
        
        return res