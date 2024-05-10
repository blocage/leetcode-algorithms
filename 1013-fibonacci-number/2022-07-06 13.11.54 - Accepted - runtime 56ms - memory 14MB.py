class Solution:
    import functools
    
    @functools.cache
    def fib(self, n: int) -> int:
        if n in (0,1):return n
        return self.fib(n - 1) + self.fib(n - 2)