class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a, b = sorted(nums[::2]), sorted(nums[1::2])[::-1]
        c = []
        t = 0
        while a or b:
            if t % 2 == 0 and a:c.append(a.pop(0))
            else:c.append(b.pop(0))
            t += 1
        return c