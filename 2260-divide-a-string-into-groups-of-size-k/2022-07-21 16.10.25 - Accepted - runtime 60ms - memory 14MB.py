class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        import textwrap
        return [f'{f:{fill}<{k}}' for f in textwrap.wrap(s, k)]