class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(f)for f in accounts)