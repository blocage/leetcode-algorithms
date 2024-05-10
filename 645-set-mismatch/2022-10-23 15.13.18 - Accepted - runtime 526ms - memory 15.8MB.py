class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        a = l * (l + 1) // 2
        d = set()
        s = 0
        for i in nums:
            if i in d:
                k = i
            else:
                d.add(i)
                s += i
        
        return k, a - s
        