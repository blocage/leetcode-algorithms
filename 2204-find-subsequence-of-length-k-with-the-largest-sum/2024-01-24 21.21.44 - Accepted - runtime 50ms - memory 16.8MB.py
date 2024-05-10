class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        return [f[1] for f in sorted(sorted(enumerate(nums), key=lambda x:x[1])[-k:])]