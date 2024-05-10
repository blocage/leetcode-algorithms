class Solution:
    def queryString(self, s: str, n: int) -> bool:
        return all(f'{f:b}'in s for f in range(1,n + 1))