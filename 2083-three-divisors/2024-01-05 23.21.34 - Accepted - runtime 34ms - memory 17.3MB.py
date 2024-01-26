class Solution:
    def isThree(self, n: int) -> bool:
        k = 1
        for i in range(2, n + 1):
            if n % i == 0:
                k += 1
            if k > 3:
                return False
        return k == 3