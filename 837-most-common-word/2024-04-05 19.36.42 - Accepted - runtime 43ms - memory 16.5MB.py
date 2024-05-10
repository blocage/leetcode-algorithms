class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        b = set(banned)
        c = Counter(filter(lambda x: x not in b, re.findall(r'\w+', paragraph.lower())))
        return c.most_common(1)[0][0]