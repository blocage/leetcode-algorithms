class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        l = []
        s = e = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - 1 == e:
                e += 1
            else:
                if s != e:
                    l.append(f'{s}->{e}')
                else:
                    l.append(str(s))
                s = e = nums[i]
        
        if s != e:
            l.append(f'{s}->{e}')
        else:
            l.append(str(s))
        return l