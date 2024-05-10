class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ready = list(range(n))
        rooms = []
        res = [0] * n
        for s,e in meetings:
            while rooms and rooms[0][0] <= s:
                t,r = heappop(rooms)
                heappush(ready, r)
            if ready:
                r = heappop(ready)
                heappush(rooms, [e, r])
            else:
                t,r = heappop(rooms)
                heappush(rooms, [t + e - s, r])
            res[r] += 1
        return res.index(max(res))