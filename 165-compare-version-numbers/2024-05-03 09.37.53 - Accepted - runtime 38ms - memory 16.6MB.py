class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        A, B = list(map(int, version1.split('.'))), list(map(int, t1 := version2.split('.')))
        for a, b in zip(A, B):
            if a > b:
                return 1
            elif b > a:
                return -1
        
        A, B = map(sum, (A, B))
        return 0 if A == B else 1 if A > B else -1