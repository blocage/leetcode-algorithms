class Solution:
    def countStudents(self, s: List[int], sa: List[int]) -> int:
        a = deque(s)
        sa = deque(sa)
        s = True
        while s:
            s = False
            for i in range(len(a)):
                st = a.popleft()
                if sa[0] == st:
                    sa.popleft()
                    s = True
                else:
                    a.append(st)


        return len(a)
        