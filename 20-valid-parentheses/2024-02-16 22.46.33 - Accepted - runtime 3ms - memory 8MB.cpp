class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> mp = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        stack<char> st;
        for (char i : s) {
            if (mp.find(i) != mp.end()) st.push(i);
            else {
                if (st.empty() || i != mp[st.top()])return false;
                st.pop();
            }
        }
    
        return st.empty();
    }
};