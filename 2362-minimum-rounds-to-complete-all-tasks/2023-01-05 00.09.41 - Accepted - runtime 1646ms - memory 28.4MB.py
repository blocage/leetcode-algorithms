class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks).values()
        return -1 if 1 in c else sum((f + 2) // 3 for f in c)