class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum)):
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[~i] = left.pop()
                    else:
                        enum[~i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
        
        