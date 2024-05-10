class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string o = "";
        string ans;
        ss >> ans;
        reverse(ans.begin(), ans.end());
        while (!ss.eof()) {
            ss >> o;
            reverse(o.begin(), o.end());
            ans.push_back(' ');
            ans += o;
        }
        
        return ans;
    }
};