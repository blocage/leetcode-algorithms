class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i in d: return i
            d.add(i)
            
        
        return i