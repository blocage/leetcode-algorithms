class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:d.pop()
            d.append(i)
            # [0 1 2 3]
            if i - k == d[0]:
                d.popleft()
            
            res.append(nums[d[0]])

        
        return res[k - 1:]