class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        for ind, i in enumerate(sorted(score, reverse=True), 1):
            d[i] = ind
        return [
            {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}.get(d[f], str(d[f]))
            for f in score]