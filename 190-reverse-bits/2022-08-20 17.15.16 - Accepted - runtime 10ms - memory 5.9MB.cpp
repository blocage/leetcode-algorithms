class Solution {
public:
    uint32_t reverseBits(uint32_t num) {
        num = ((num & 0x55555555) << 1) | ((num & 0xAAAAAAAA) >> 1);
        num = ((num & 0x33333333) << 2) | ((num & 0xCCCCCCCC) >> 2);
        num = ((num & 0x0F0F0F0F) << 4) | ((num & 0xF0F0F0F0) >> 4);
        num = ((num & 0x00FF00FF) << 8) | ((num & 0xFF00FF00) >> 8);
        num = ((num & 0x0000FFFF) << 16) | ((num & 0xFFFF0000) >> 16);

        return num;
    }
};