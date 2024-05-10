class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 1
        res = 0
        l = len(arr)
        while i <= l:
            res += sum(sum(arr[f:i+f])for f in range(l - i + 1))
            i += 2
        return res