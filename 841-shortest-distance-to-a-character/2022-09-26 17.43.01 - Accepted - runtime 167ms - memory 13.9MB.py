class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [ind for ind,f in enumerate(s)if f == c]
        return [min(abs(ind - i)for i in indices)for ind,f in enumerate(s)]