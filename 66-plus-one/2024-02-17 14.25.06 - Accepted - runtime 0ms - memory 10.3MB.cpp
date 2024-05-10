class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int high = digits.size() - 1;
        while(high >= 0){ // 19999999
            if(digits[high] == 9) {
                digits[high] = 0;
                if (!high){
                    digits.push_back(0);
                    digits[0] = 1;
                }
            }
            else{
                digits[high]++;
                return digits;
            }
            high--;
        }
        return digits;
    }
};