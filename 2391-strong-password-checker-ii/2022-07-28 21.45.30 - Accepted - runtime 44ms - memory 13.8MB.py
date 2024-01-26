class Solution:
    def strongPasswordCheckerII(self, p: str) -> bool:
        a=b=c=d=False
        prev = None
        for i in p:
            if i == prev:return False
            elif i.islower():a=1
            elif i.isupper():b=1
            elif i.isdigit():c=1
            else:d=1
            prev = i
            
        
        return len(p) > 7 and a and b and c and d