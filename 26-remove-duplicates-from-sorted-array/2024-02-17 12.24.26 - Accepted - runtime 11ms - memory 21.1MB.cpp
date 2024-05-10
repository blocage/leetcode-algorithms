class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int r = 0;
        for (int i=1;i < nums.size();i++)
        if (nums[i] != nums[r]) nums[++r] = nums[i];
        return ++r;
    }
};