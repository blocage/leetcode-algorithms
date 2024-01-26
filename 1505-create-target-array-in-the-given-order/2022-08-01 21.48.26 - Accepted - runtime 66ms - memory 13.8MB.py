class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = []
        for a,b in zip(nums, index):
            l.insert(b, a)
        return l