class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res, pos = 10**6+1, {}
        for i, c in enumerate(cards):
            if c in pos:
                res = min(res, i - pos[c] + 1)
            pos[c] = i
        
        return res % (10**6+1) or -1