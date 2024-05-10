class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(Counter(word).values())
        if (len(cnt) == 1):
            return list(cnt.keys())[0] == 1 or list(cnt.values())[0] == 1
        if (len(cnt) == 2):
            f1, f2 = min(cnt.keys()), max(cnt.keys())
            return (f1 + 1 == f2 and cnt[f2] == 1) or (f1 == 1 and cnt[f1] == 1)
        return False