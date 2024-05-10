class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res = 0 
        times = 0
        l = len(arr)
        for i in range(l):
            times = times-(i+1)//2+(l-i+1)//2
            res += times*arr[i]
        return res