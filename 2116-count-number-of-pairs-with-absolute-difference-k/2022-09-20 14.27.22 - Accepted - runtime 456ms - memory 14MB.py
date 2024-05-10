class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        r = 0
        l = len(nums)
        for i in range(l):
            for j in range(i, l):
                if i == j:continue
                r += abs(nums[i] - nums[j]) == k

        return r