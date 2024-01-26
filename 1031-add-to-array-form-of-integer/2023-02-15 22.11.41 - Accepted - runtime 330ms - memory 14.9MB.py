class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int,str(int(''.join(map(str, num))) + k)))