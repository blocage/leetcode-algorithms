class Solution:
    def dailyTemperatures(self, te: List[int]) -> List[int]:
        r = [0] * len(te)
        stack = []
        for i, t in enumerate(te):
            while stack and stack[-1][1] < t:
                ind, temp = stack.pop()
                r[ind] = i - ind
            stack.append((i, t))
        
        return r