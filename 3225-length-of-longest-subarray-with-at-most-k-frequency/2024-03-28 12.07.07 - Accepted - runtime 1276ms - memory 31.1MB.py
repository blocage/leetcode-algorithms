class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        c = Counter()
        res = left = 0
        for right in range(len(nums)):
            c[nums[right]] += 1
            while c[nums[right]] > k:
                c[nums[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res