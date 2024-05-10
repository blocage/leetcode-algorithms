class Solution:
    def kidsWithCandies(self, candies: List[int], t: int) -> List[bool]:
        r = max(candies)
        return [f + t >= r for f in candies]
