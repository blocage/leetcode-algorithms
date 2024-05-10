class Solution {
public:
    string longestPalindrome(string s) {
        int l = s.size(), wl = 0;
        string w;
        for (int i = 0;i < l;i++){
            for (int u = 0;u < 2;u++){
                int j = i, k = i + u;
                while (j >= 0 && l > k && s[j] == s[k]){
                    j--;
                    k++;
                }
                if (k - j - 1 > wl){
                    wl = k - j - 1;
                    w = s.substr(j + 1, k - j - 1);
                }
            }
        }
        return w;
    }
};