class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for ind, i in enumerate(nums):
            if i in D:
                return [D[i], ind]
            D[target - i] = ind
        
        return [-1]