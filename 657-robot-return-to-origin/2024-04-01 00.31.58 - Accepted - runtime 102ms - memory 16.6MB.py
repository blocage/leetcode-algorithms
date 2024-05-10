class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for i in moves:
            x += [[0, -1][i == 'L'], 1][i == 'R']
            y += [[0, -1][i == 'D'], 1][i == 'U']
        
        return not x and not y