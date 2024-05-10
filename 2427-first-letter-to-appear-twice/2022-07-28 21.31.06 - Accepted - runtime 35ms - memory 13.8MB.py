class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = ''
        for i in s:
            if i in a:return i
            a += i
        return i