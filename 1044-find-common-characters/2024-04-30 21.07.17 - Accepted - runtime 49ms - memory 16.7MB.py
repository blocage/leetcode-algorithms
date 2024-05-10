class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = Counter(words[0])
        for i in words[1:]:
            t = Counter(i)
            for j in list(d.keys()):
                if j not in i:
                    del d[j]
                else:
                    d[j] = min(d[j], t[j])
        
        res = []
        for a,b in d.items():
            res.extend([a] * b)
        return res