class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = set()
        for i in nums:
            if i in n:
                return i
            n.add(i)