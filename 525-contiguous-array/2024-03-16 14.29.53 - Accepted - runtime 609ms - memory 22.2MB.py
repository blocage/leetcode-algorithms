class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = c = 0
        d = {0: 0}
        for ind, i in enumerate(nums, 1):
            if i == 0:c -= 1
            else:c += 1
            if c in d:
                res = max(res, ind - d[c])
            else:
                d[c] = ind
        return res