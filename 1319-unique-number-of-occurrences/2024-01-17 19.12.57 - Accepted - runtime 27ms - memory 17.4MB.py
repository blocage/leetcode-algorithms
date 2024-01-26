class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        k = Counter(arr).values()
        return len(k) == len(set(k))