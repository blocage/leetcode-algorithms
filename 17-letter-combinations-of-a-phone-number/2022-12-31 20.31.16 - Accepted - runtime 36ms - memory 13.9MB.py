class Solution:
    d = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        res = []
        self.dfs(digits, "", res)
        return res
    
    def dfs(self, digits: str, path: str, res: list[str]) -> None:
        if not digits:
            res.append(path)
            return
        
        for i in self.d[digits[0]]:
            self.dfs(digits[1:], path + i, res)