class Solution:
    def calculate(self, s: str) -> int:
        from re import compile, findall
        regex = compile(r'\([^\(\)]+\)')
        while a := findall(regex, s):
            for i in a:
                s = s.replace(i, str(eval(i)))
            
        
        return eval(s)