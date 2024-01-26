class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        a = collections.Counter(ranks).most_common(1)[0][1]
        if a >= 3:
            return 'Three of a Kind'
        elif a == 2:
            return 'Pair'
        else:
            return 'High Card'