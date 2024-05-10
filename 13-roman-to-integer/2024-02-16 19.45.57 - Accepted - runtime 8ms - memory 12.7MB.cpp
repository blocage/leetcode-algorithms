class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> rn = {
                    {'I', 1}, 
                    {'V', 5}, 
                    {'X', 10}, 
                    {'L', 50}, 
                    {'C', 100}, 
                    {'D', 500}, 
                    {'M', 1000}
        };
        int r = 0;
        for (int ind=0; ind < s.size(); ++ind){
            if ((ind + 1) == s.size() || rn[s[ind]] >= rn[s[ind + 1]]){
                r += rn[s[ind]];
            }
            else {
                r -= rn[s[ind]];
            }
        }
        return r;
    }
};