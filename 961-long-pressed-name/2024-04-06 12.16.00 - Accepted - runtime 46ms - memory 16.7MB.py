class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a,b = map(lambda x: list((A, len(list(B))) for A,B in groupby(x)), (name, typed))
        if len(a) != len(b):
            return False
        for (i, j), (I, J) in zip(a, b):
            if i != I or j > J:
                return False
        return True