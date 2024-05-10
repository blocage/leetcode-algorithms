class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        visited = [0] * 201
        r = 0
        for i in nums:
            if i >= 2 * diff:
                r += visited[i - diff] and visited[i - 2 * diff]
            
            visited[i] = 1

        return r