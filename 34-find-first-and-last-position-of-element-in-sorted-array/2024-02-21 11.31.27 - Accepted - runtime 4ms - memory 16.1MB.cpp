#pragma GCC optimize("Ofast")
#pragma GCC target("avx2")
int init = [](){
    cin.tie(nullptr)->sync_with_stdio(false);
    return 14122021;
}();

class Solution {
public:
    vector<int> searchRange(vector<int>& a, int t) {
        if(!binary_search(a.begin(), a.end(), t)) {
            return {-1, -1};
        }
        return {
            static_cast<int>(lower_bound(a.begin(), a.end(), t) - a.begin()),
            static_cast<int>(upper_bound(a.begin(), a.end(), t) - a.begin() - 1)
        };
    }
};