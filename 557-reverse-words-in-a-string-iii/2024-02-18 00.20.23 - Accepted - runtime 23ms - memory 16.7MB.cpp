class Solution {
public:
    string reverseWords(string s) {
        string res, tmp;
        for (char i: s){
            if (i == ' '){
                reverse(tmp.begin(), tmp.end());
                res += tmp + " ";
                tmp = "";
            }
            else tmp += i;
        }
        reverse(tmp.begin(), tmp.end());
        return res + tmp;
    }
};