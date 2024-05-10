class Solution {
public:
    char findTheDifference(string s, string t) {
        char a = 0;
        for (int i = 0;i < s.size(); i++) a += t[i] - s[i];
        return a + t[t.size() - 1];
    }
};