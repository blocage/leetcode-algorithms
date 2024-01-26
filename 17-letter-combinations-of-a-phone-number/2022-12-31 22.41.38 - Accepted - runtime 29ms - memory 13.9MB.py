class Solution:
    d = {'2': 'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        self.dfs(digits, '', res, 0, len(digits))
        return res
    
    def dfs(self, digits: str, combo: str, res: List[str], index: int, max_index: int) -> None:
        if index == max_index:
            return res.append(combo)

        for i in self.d[digits[index]]:
            self.dfs(digits, combo + i, res, index + 1, max_index)