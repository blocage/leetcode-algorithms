class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int r = 0;
        for (int ind=0;ind < nums.size();){
            if (nums[ind] == val)nums.erase(nums.begin()+ind);
            else{r++; ind++;}
        }
        return r;
    }
};