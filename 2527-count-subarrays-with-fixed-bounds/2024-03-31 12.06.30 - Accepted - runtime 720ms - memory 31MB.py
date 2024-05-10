class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0; m = M = last = -1
        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK: last = i
            if nums[i] == minK: m = i
            if nums[i] == maxK: M = i
            res += max(0, min(m, M) - last)

        
        return res
