class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            n = sum(map(lambda x:int(x)**2, str(n)))
            if n == 1:
                    return True
        return False
        