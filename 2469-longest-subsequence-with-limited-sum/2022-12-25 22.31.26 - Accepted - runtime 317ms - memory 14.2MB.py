class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in queries:
            s = c = 0
            for j in nums:
                s += j
                if s > i:
                    break
                c += 1
            res.append(c)
        
        return res