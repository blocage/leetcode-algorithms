class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people) - 1
        res = 0
        while lo <= hi:
            res += 1
            if people[hi] + people[lo] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
        
        return res