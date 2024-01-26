class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(str(f)for f in digits)) + 1
        return list(str(a))