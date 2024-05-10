class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = df = 0
        for ind, i in enumerate(nums, start = 1):
            d += ind - i
            df += ind * ind - i * i
        
        s = df // d
        return (s - d) // 2, (s + d) // 2