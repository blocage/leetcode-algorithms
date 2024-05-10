class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char i: s){
            if (i == '(' || i == '{' || i == '[')st.push(i);
            else{
                if (st.empty() ||
                    (i == ')' && st.top() != '(') ||
                    (i == ']' && st.top() != '[') ||
                    (i == '}' && st.top() != '{')
                  ) return false;
                st.pop();
            }
        }
        return st.empty();
    }
};