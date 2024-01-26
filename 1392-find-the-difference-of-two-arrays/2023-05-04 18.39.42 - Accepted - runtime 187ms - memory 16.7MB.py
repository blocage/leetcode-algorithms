class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a, b = set(nums1), set(nums2)
        return a.difference(b), b.difference(a)