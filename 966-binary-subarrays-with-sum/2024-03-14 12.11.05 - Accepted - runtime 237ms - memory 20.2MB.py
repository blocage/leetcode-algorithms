class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in nums:
            psum += i
            res += c[psum - goal]
            c[psum] += 1
        return res