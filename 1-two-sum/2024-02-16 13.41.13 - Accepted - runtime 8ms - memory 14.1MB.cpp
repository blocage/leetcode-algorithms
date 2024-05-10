class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indices;
        for (int ind = 0; ind < nums.size(); ++ind) {
            int t = target - nums[ind];
            if (indices.find(t) != indices.end()) {
                return {indices[t], ind};
            }
            indices[nums[ind]] = ind;
        }
        return {};
    }
};