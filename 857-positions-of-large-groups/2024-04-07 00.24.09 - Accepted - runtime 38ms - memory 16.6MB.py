class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        r = []
        count = last = 0
        curr = ''
        for i in range(len(s)):
            if curr == s[i]:
                count += 1
            else:
                if count > 2:
                    r += (last, i - 1),
                last = i
                curr = s[i]
                count = 1
        if count > 2:r += (last, i),

        return r