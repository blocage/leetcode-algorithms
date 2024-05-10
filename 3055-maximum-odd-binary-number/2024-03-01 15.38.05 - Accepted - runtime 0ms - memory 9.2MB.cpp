class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int o = count(s.begin(), s.end(), '1');
        int z = s.length() - o;

        return string(o - 1, '1') + string(z, '0') + "1";
    }
};