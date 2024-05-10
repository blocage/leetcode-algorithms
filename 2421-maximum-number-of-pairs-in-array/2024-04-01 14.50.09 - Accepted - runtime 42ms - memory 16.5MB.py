class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums).values()
        a = b = 0
        for i in c:
            i, j = divmod(i, 2)
            a += i
            b += j
        
        return [a, b]