class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [[1]]
        for i in range(1, rowIndex + 1):
            t = [1]
            for j in range(1, len(l[i - 1])):
                t.append(sum(l[i - 1][j-1 : j+1]))
            t += [1]
            l.append(t)
        return l[rowIndex]