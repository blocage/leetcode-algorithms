class Solution:
    def findComplement(self, num: int) -> int:
        return int(f'{num:b}'.translate(str.maketrans({'1':'0', '0':'1'})), 2)