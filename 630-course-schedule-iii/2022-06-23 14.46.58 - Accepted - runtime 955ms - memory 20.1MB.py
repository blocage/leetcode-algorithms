class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        valid_courses, curr = [], 0
        courses.sort(key=lambda x:x[1])
        for dur, ld in courses:
            heapq.heappush(valid_courses, -dur)
            curr += dur
            if curr > ld: curr += heapq.heappop(valid_courses)
        
        return len(valid_courses)
            