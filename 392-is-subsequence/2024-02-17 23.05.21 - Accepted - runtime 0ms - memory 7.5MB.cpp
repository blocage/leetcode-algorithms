class Solution {
public:
    bool isSubsequence(string s, string t) {
        int a = 0, b = 0;
        while (a < s.size() && b < t.size())if (s[a] == t[b++]) a++;
        return a == s.size();
    }
};