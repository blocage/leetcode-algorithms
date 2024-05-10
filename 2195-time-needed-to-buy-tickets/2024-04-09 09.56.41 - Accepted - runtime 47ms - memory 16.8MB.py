class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        l = len(tickets)
        while tickets[k]:
            for ind in range(l):
                if tickets[ind]:
                    res += 1
                    tickets[ind] -= 1
                if not tickets[k]:
                    return res
        

        return res