class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if not i % 3:
                if not i % 5:
                    res.append('FizzBuzz')
                else:
                    res.append('Fizz')
                    
            elif not i % 5:
                res.append('Buzz')
            else:
                res.append(str(i))
        
        return res