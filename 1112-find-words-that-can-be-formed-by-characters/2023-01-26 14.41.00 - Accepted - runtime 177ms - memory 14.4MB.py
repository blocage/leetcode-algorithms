class Solution:
    def countCharacters(self, words: List[str], c: str) -> int:
        c = collections.Counter(c)
        res = 0
        for j in words:
            good = True
            i = collections.Counter(j).items()
            for char, counter in i:
                if char not in c or c[char] < counter:
                    good = False
                    break
            
            if good:
                for char, counter in i:
                    res += counter
    

        return res