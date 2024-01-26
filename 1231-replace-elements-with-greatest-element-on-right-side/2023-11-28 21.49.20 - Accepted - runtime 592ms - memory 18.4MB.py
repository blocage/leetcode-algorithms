class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        g = 0
        for i in arr[::-1]:
            if i > g:
                g = i
            res.append(g)
        res.pop()

        return res[::-1]