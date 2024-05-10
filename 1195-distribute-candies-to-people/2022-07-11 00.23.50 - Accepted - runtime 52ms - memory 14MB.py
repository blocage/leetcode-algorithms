class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        n = 0
        while True:
            for i in range(num_people):
                c = min(num_people * n + i + 1, candies)
                res[i] += c
                candies -= c
                if candies <= 0: return res
            n += 1