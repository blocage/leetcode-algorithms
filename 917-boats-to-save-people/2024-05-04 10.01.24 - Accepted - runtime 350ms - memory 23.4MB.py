class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        l, r = 0, len(people) - 1
        people.sort()
        while l <= r:
            while people[r] > limit: r -= 1
            if people[r] + people[l] <= limit:
                res += 1
                r -= 1
                l += 1
            else:
                res += 1
                r -= 1
        return res