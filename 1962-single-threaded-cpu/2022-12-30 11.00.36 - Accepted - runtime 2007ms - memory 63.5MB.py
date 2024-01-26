class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        l = sorted((a, b, ind) for ind, (a, b) in enumerate(tasks))
        res = []
        next_tasks = []
        curr_time = curr_ind = 0
        n = len(tasks)
        while n > curr_ind or next_tasks:
            if not next_tasks and curr_time < l[curr_ind][0]:
                curr_time = l[curr_ind][0]
            
            while n > curr_ind and curr_time >= l[curr_ind][0]:
                _, b, original_index = l[curr_ind]
                heapq.heappush(next_tasks, (b, original_index))
                curr_ind += 1
            
            b, ind = heapq.heappop(next_tasks)
            curr_time += b
            res.append(ind)
        
        return res