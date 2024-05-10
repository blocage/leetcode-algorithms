class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = [sum(map(int, str(f))) for f in nums]
        res = -1
        l = defaultdict(list)
        for ind, i in enumerate(n):l[i].append(ind)
        for i in l.values():
            t = sorted(i, key=lambda x: -nums[x])[:2]
            if len(t) == 2:
                res = max(res, nums[t[0]] + nums[t[1]])
        return res