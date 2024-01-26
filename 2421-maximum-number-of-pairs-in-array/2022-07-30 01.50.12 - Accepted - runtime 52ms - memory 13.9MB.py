class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        a=b=0
        for i in d.values():
            a += i%2
            b += i // 2
        
        return b, a