class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = list(map(set, nums))
        t = l[0]
        for i in l[1:]:
            t = t.intersection(i)
        return sorted(t)
        