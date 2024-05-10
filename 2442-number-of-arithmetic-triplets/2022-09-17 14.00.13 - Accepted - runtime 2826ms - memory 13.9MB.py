class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        r = 0
        for k in range(l := len(nums)):
            for j in range(k):
                for i in range(j):
                    if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                        r += 1

        return r