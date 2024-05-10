class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0, high = s.size() - 1;
        while (high >= 0 && s[high] == ' ')high--;
        while (high >= 0 && s[high--] != ' ')res++;
        return res;
    }
};