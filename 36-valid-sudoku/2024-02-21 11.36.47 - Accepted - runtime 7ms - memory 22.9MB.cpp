class Solution
{
public:
    bool isValidSudoku(vector<vector<char> > &board)
    {
        int u1[9][9] = {0}, u2[9][9] = {0}, u3[9][9] = {0};
        
        for(int i = 0; i < board.size(); ++ i)
            for(int j = 0; j < board[i].size(); ++ j)
                if(board[i][j] != '.')
                {
                    int num = board[i][j] - '0' - 1, k = i / 3 * 3 + j / 3;
                    if(u1[i][num] || u2[j][num] || u3[k][num])
                        return false;
                    u1[i][num] = u2[j][num] = u3[k][num] = 1;
                }
        
        return true;
    }
};