class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [f'{h}:{m:02}' for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == turnedOn]