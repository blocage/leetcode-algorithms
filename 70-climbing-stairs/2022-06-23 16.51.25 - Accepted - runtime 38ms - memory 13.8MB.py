class Solution:
    stairs = [0] * 45
    def climbStairs(self, n: int) -> int:
        arr = [0] * (n+1)
        for i in range(n+1):
            if i < 3:
                arr[i] = i
            else:
                arr[i] = arr[i-1] + arr[i-2]
        
        return arr[-1]