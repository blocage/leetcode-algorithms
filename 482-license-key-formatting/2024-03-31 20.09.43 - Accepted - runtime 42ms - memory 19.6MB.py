class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = ''.join(f.upper() for f in s if f.isalnum())[::-1]
        return '-'.join(s[f: f + k] for f in range(0, len(s), k))[::-1]