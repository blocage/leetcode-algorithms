class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = c.most_common(1)[0][1]
        return sum(v for k,v in c.items() if v == m)
        