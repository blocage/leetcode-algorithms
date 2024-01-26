class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        s, e = 0, 2
        l = len(nums)
        if l % 2: return False
        while e <= l:
            a,b = nums[s:e]
            if a != b: return False
            s += 2
            e += 2
        
        return True
        