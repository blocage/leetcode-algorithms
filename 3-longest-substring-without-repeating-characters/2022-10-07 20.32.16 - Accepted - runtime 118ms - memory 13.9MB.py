class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        start = res = 0
        for i in range(len(s)):
            if s[i] in visited:
                start = max(start, visited[s[i]] + 1)
            visited[s[i]] = i
            res = max(res, i - start + 1)
        return res