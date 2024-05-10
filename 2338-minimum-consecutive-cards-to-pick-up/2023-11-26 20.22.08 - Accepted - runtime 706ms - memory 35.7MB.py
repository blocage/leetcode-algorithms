class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res, r = 10e7, {}
        for i in range(len(cards)):
            if cards[i] in r:
                res = min(res, i - r[cards[i]] + 1)
            r[cards[i]] = i
        
        return res if res != 10e7 else -1