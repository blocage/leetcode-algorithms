class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, prod, res = 0, 1, 0
        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            
            res += right - left + 1
        

        return res