class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c = collections.Counter(tasks)
        res = 0
        for _, count in c.items():
            t = count - 3
            k = count - 4
            if count % 3 == 0:
                res += count // 3
            elif (count % 3) % 2 == 0:
                res += count // 3 + 1
            elif k > 0 and k % 3 == 0:
                res += k // 3 + 2
            elif count % 2 == 0:
                res += count // 2
            elif t > 0 and t % 2 == 0:
                res += t // 2 + 1
            else:
                return -1
        
        return res