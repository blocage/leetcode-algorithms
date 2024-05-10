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
        for (int i=0; i < s.size(); ++i){ // VI
            if (rn[s[i]] >= rn[s[i + 1]]){
                r += rn[s[i]];
            }
            else {
                r -= rn[s[i]];
            }
        }
        return r;
    }
};