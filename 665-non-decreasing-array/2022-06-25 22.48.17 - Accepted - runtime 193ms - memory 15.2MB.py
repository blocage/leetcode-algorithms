class Solution:
    def checkPossibility(self, A):
        p, n = -1, len(A)
        for i in range(n - 1):
            if A[i] > A[i+1]:
                if p != -1: return False
                p = i

        return p in [-1, 0, n-2] or A[p-1] <= A[p+1] or A[p] <= A[p+2]