class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c ** .5) + 1):
            j = (c - i * i) ** .5
            if j % 1 == 0:
                return True
        
        return False