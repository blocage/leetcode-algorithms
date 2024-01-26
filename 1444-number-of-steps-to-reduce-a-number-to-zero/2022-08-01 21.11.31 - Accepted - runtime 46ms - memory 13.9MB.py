class Solution:
    def numberOfSteps(self, n: int) -> int:
        r = 0
        while n:
            r += 1
            if n % 2:n -= 1
            else:n //= 2
        
        return r