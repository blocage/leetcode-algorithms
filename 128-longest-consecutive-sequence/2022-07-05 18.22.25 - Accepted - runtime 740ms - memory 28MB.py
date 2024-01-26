class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        l = len(nums)
        if not l: return 0
        curr = res = 1
        for i in range(l - 1):
            if nums[i] + 1 == nums[i + 1]:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
                
        return max(res, curr)