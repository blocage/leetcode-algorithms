from bisect import bisect

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        arr = list(num)
        for _ in range(k):
            brr = [arr.pop()]
            while arr[-1] >= brr[-1]:
                brr.append(arr.pop())
            i = bisect(brr, arr[-1])
            arr[-1], brr[i] = brr[i], arr[-1]
            arr += brr
        
        count = 0
        for item in num:
            i = arr.index(item)
            count += i
            arr.pop(i)

        return count