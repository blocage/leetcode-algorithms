class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        l = {}
        for i in nums:
            d = sum(map(int, str(i)))
            if d in l:
                res = max(res, i + l[d])
                l[d] = max(l[d], i)
            else:
                l[d] = i

        return res