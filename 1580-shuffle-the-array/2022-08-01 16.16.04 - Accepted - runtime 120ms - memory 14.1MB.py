class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for a,b in zip(nums[:n], nums[n:]):
            res.append(a)
            res.append(b)
        
        return res