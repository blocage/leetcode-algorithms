class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(f - i) > d for f in arr2) for i in arr1)