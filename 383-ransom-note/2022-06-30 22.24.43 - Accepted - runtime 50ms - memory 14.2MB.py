class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(f)<=magazine.count(f)for f in set(ransomNote))