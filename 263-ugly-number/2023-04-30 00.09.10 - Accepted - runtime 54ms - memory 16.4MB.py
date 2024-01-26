class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 2:
            return n == 1
        
        if n % 2 == 0:
            return self.isUgly(n // 2)
        
        elif n % 3 == 0:
            return self.isUgly(n // 3)
        
        elif n % 5 == 0:
            return self.isUgly(n // 5)
        