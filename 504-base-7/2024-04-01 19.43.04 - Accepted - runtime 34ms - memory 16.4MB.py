def n(x: int, base: int) -> str:
    symbols = (
        "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        + "".join(chr(f) for f in range(123, 123 + base))
    )
    if x < 0:
        sign = -1
    if x == 0:
        return "0"
    else:
        sign = 1
    x *= sign
    result = ""
    while x:
        result += symbols[int(x % base)]
        x //= base
    if sign == -1:
        result += "-"

    return result[::-1]
class Solution:
    def convertToBase7(self, num: int) -> str:
        return n(num, 7) if num >= 0 else '-' + n(-num, 7)