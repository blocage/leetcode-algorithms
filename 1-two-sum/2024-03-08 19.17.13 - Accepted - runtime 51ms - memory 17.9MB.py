class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind, i in enumerate(nums):
            if i in d:
                return [d[i], ind]
            
            d[target - i] = ind
        
        return 1
