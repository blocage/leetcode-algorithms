class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        from string import ascii_lowercase as ass
        k = ' '
        for i in key:
            if i not in k:k+=i
        
        return message.translate(str.maketrans(k[1:],ass))