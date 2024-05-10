class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(Counter, (nums1, nums2))
        res = []
        for i in a:
            if i in b:
                res += [i] * min(a[i], b[i])
        
        return res