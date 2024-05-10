class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return s.lower() not in ('inf', '-inf', '+inf', 'infinity', '-infinity', '+infinity', 'nan', '-nan')
        except:
            return False