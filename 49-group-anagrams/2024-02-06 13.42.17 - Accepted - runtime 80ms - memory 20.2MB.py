class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            d[key].append(i)

        
        return d.values()