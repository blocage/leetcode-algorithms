class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(i['tcn'.index(ruleKey[0])] == ruleValue for i in items)