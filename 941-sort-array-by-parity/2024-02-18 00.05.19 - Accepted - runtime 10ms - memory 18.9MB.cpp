class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int even=-1;
        for(int& x: nums) if(!(x&1)) swap(nums[++even], x);
        return nums;
    }
};