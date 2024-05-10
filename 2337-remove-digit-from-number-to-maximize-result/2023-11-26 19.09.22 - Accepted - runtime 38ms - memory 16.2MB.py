class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l = [number[1:]] if number[0] == digit else []
        for i in range(1, len(number)):
            if number[i] == digit:
                l.append(number[:i] + number[i + 1: ])
        return max(l)