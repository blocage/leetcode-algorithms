class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        while (low < high){
            while (low < high && nums[low] % 2 == 0) low++;
            while (low < high && nums[high] % 2)high--;
            swap(nums[low], nums[high]);
        }
        return nums;
    }
};