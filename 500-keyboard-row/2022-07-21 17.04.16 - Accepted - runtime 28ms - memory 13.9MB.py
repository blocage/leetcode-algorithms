class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l = ['qwertyuiop','asdfghjkl','zxcvbnm']
        t = []
        for word in words:
            if any(all(char in f for char in word.lower()) for f in l):
                t += word,
        
        return t