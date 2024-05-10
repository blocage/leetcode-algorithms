class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for i in nums:
            if i == 0:
                return 0
            i = 1 if i > 0 else -1
            s *= i
        return s