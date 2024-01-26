class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        @functools.lru_cache(None)
        def solve(i: int, k: int) -> int:
            if k == 0 or i == n: return 0
            res, curr = solve(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                curr += piles[i][j]
                res = max(res, curr + solve(i + 1, k - j - 1))
            return res

        return solve(0, k)