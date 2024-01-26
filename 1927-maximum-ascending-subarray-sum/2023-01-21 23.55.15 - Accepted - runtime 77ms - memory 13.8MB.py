class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = -2E6
        prev = prev_sum = nums[0]
        for i in nums[1:]:
            if prev < i:
                prev_sum += i
            else:
                res = max(res, prev_sum)
                prev_sum = i
            
            prev = i

        return max(res, prev_sum)
            