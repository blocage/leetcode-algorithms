def is_prime_optimized(n: int) -> bool:
    if n % 2 == 0 or n < 2:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        l = 0
        for i in range(len(nums)):
            if is_prime_optimized(nums[i][i]) and nums[i][i] > l:
                l = nums[i][i]
            if is_prime_optimized(nums[i][~i]) and nums[i][~i] > l:
                l = nums[i][~i]
        
        return l