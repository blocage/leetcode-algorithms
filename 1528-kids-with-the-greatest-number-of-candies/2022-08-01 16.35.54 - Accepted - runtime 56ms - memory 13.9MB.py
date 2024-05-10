class Solution:
    def kidsWithCandies(self, candies: List[int], e: int) -> List[bool]:
        m = max(candies)
        return [f+e >= m for f in candies]