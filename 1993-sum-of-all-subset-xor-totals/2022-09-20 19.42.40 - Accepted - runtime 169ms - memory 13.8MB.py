class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r = 0
        for i in range(1, len(nums) + 1):
            for f in itertools.combinations(nums, r=i):
                k = 0
                for n in f:
                    k ^= n
                r += k
        return r