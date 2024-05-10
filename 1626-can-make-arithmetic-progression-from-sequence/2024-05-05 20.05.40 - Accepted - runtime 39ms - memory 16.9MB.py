class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        t, prev = arr[0] - arr[1], arr[1]
        for i in arr[2:]:
            if prev - i != t: return False
            prev = i
        return True