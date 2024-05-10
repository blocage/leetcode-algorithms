class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u = l = 0
        for i in word:
            if i.islower():
                l += 1
            else:
                u += 1
        
        return not l or not u or u == 1 and word[0].isupper()