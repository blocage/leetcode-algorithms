class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Vertical
        for i in board:
            nums = []
            for j in i:
                if j.isdigit():
                    if j in nums:
                        return False
                    
                    nums.append(j)
        # Horizontal
        for i in zip(*board):
            nums = []
            for j in i:
                if j.isdigit():
                    if j in nums:
                        return False
                    
                    nums.append(j)
        # Grid
        for j in (1, 4, 7):
            for i in (1, 4, 7):
                nums = []
                for y in range(j - 1, j + 2):
                    for x in range(i - 1, i + 2):
                        if board[y][x].isdigit():
                            if board[y][x] in nums:
                                return False
                            
                            nums.append(board[y][x])



        return True