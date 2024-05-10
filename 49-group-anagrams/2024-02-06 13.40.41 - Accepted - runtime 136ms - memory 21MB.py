class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            key = str(sorted(Counter(i).items()))
            d[key] = d.get(key, []) + [i]

        
        return d.values()