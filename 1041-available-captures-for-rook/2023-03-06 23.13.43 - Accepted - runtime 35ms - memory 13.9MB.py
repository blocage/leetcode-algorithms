class Solution:
    def find_rook(self, board: List[List[str]]) -> tuple[int, int]:
        for y,line in enumerate(board):
            for x,i in enumerate(line):
                if i.isalpha():
                    if i == 'R':
                        return x, y
    def numRookCaptures(self, board: List[List[str]]) -> int:
        X, Y = self.find_rook(board)
        h = v = ''
        for y,line in enumerate(board):
            if y == Y:
                v = ''.join(line)
            for x,i in enumerate(line):
                if X == x:
                    h += i
        
        r = re.compile(r'p\.*R')
        r2 = re.compile(r'R\.*p')
        return len(re.findall(r, h)) + len(re.findall(r2, h)) + len(re.findall(r, v)) + len(re.findall(r2, v))