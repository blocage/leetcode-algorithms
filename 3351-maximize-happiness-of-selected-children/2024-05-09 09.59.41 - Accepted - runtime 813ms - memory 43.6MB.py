class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        s = 0
        for i in range(k):
            t = max(happiness[~i] - i, 0)
            if not t: return s
            s += t
        return s