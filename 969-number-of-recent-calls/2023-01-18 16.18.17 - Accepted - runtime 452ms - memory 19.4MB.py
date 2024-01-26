class RecentCounter:

    def __init__(self):
        self.min = -3000
        self.pings: list[int] = []
        self.res = 0

    def ping(self, t: int) -> int:
        self.pings.append(t)
        self.min = t - 3000
        self.res += 1
        for i in range(self.res):
            if self.pings[i] >= self.min:
                self.pings = self.pings[i:]
                break
            self.res -= 1
        return self.res
            