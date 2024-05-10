class Solution:
    def calculate(self, s: str) -> int:
        return int(eval(s.replace('/', '//')))
