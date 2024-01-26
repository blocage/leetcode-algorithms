class Solution:
    def numSquares(self, n: int) -> int:
        if (n ** .5) % 1 == 0:
            return 1

        while 2:
            c = n
            for i in (2, 5):
                if c % i == 0:
                    c >>= int(math.log(c & -c, i))
        
            while c % 9 == 0:
                c //= 9

            if c % 3 == 0: 
                break

            if c in {0, 1, 13, 17}: 
                return 2

            i, j = 0, int(c**.5)

            while i <= j:
                temp = i * i + j * j
                if temp == c: return 2
                elif temp > c: j-= 1
                else: i += 1

            break

        while n % 4 == 0:
            n //= 4

        return 3 if n % 8 != 7 else 4