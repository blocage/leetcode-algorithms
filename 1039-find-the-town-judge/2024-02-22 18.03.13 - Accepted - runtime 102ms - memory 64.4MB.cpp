class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> s(n + 1, 0);
        for (int i=0; i < trust.size(); i++){
            s[trust[i][0]]--;
            s[trust[i][1]]++;
        }
        for (int i=1; i <= n; i++){
            if (s[i] == n - 1) return i;
        }
        return -1;
    }
};