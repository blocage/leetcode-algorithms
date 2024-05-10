class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        ko = prices[0]
        for i in range(1, len(prices)):
            if (a := prices[i] - ko) > res:
                res = a
            if ko > prices[i]:
                ko = prices[i]
        return res