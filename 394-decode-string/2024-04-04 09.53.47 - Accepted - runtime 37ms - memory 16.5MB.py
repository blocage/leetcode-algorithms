class Solution:
    def decodeString(self, s: str) -> str:
        from re import compile, sub, search
        regex = compile(r'(\d+)\[(\w+)\]')
        while search(regex, s):
            s = sub(regex, lambda x: int(x.group(1)) * x.group(2), s) 
        return s