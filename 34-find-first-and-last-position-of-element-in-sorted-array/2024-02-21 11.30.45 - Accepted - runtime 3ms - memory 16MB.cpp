class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == target){
                int j = i;
                while(i < nums.size() && nums[i] == target)i++;
                return {j, i - 1};
            }
        }
        return {-1, -1};
    }
};