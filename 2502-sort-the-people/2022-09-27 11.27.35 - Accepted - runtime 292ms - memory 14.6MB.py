class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for name,height in sorted(zip(names, heights), key=lambda x:-x[1])]