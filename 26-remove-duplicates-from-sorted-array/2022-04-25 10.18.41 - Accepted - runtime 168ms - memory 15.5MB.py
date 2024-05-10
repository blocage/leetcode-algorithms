class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        k = 0
        while k < len(nums) - 1:
            if nums[k] == nums[k + 1]:
                nums.pop(k)
            else:
                k += 1
        else:
            k += 1

        return k
        