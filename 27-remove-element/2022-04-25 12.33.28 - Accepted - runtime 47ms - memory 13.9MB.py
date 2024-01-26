class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in nums.copy():
            if i == val:nums.remove(i)
            else:k += 1
        return k