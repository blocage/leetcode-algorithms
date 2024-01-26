class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(p: str, left: int, right: int, res: List[str] = []) -> List[str]:
            if left:solve(p + '(', left - 1, right)
            if right > left:solve(p + ')', left, right - 1)
            if not right:res += p,
            return res
        
        return solve('', n, n)