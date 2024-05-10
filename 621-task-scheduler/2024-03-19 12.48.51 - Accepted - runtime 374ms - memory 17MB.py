class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = defaultdict(int)
        count = 0
        for i in tasks:
            c[i] += 1
            count = max(count, c[i])
        res = (count - 1) * (n + 1)
        for i in c: 
            if c[i] == count: res += 1
        
        return max(res, len(tasks))
        