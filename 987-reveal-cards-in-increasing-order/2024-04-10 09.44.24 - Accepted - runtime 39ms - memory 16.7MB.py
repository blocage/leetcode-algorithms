class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque()
        for x in sorted(deck)[::-1]:
            d.rotate()
            d.appendleft(x)
        return d