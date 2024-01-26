class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return sum((coins := coins - f) >= 0 for f in sorted(costs))