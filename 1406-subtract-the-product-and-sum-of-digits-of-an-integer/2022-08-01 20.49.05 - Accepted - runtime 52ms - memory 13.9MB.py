class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return eval('*'.join(str(n))) - eval('+'.join(str(n)))