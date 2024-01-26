class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = []
        for a,b in zip(nums[::2], nums[1::2]):
            l += [b] * a
        
        return l