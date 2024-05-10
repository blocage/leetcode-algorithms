class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = res = left = 0
        m = max(nums)
        for right in range(len(nums)):
            count += nums[right] == m
            while count == k:
                count -= nums[left] == m
                left += 1
            res += left

        return res
        