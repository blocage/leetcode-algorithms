class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = Counter(tasks).values()
        return -1 if 1 in c else sum((a + 2) // 3 for a in c)