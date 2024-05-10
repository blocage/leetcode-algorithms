class Solution:
    def closing(self, current_open: str, check_val: str) -> bool:
        if current_open == '(' and check_val == ')':return True
        if current_open == '[' and check_val == ']':return True
        if current_open == '{' and check_val == '}':return True
        return False
    
    def isValid(self, s: str) -> bool:
        opened = ''
        for i in s:
            if i in '([{':
                opened += i
            else:
                if not opened or not self.closing(opened[-1], i):
                    return False
                else:
                    opened = opened[:-1]

        return opened == ''
        