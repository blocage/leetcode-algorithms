class BrowserHistory:

    def __init__(self, homepage: str):
        self.h = [homepage]
        self.c = 0

    def visit(self, url: str) -> None:
        self.c += 1
        self.h = self.h[:self.c]
        self.h.append(url)
        

    def back(self, steps: int) -> str:
        self.c = max(self.c - steps, 0)
        return self.h[self.c]

    def forward(self, steps: int) -> str:
        self.c = min(self.c + steps, len(self.h) - 1)
        return self.h[self.c]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)