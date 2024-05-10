class Solution {
public:
    int missingNumber(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        int n=nums.size();
        int sum;
        sum=(n*(n+1))/2;
        int ans=sum-accumulate(nums.begin(),nums.end(),0);
        return ans;
    }
};